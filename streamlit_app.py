import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
import requests

api_key = st.secrets["pass"]


st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
Web App URL: <https://template.streamlit.app>
GitHub Repository: <https://github.com/giswqs/streamlit-multipage-template>
"""

#st.sidebar.title("About")
#st.sidebar.info(markdown)
#logo = "https://i.imgur.com/UbOXYAU.png"
#st.sidebar.image(logo)

# Customize page title
st.title("World Weather")

df2 = pd.read_csv('th.csv')
#st.write(len(df2))
df2 = df2.dropna()
st.write(df2)
#for i in range(3):
#    st.write(df2.loc[i, ['lat']])

# st.markdown(
#     """
#     This multipage app template demonstrates various interactive web apps created using [streamlit](https://streamlit.io) and [leafmap](https://leafmap.org). It is an open-source project and you are very welcome to contribute to the [GitHub repository](https://github.com/giswqs/streamlit-multipage-template).
#     """
# )

#st.header("Instructions")

markdown = """
"""

#st.markdown(markdown)

#m = leafmap.Map(minimap_control=True)
#m = leafmap.Map(center=(14.5, 101.5))
m = leafmap.Map(height="200px", width="50px",
                draw_control=False,
                measure_control=False,
               )

# Define a list of cities to get temperature data for
cities = ["New York", "Paris", "Tokyo", "Sydney", "Cape Town", "Rio de Janeiro", "Moscow", "Dubai", "Mumbai", "Cairo", "Bangkok"]

url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
url2 = "http://api.openweathermap.org/data/2.5/air_pollution?lat={}&lon={}&appid={}"
url3 = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}"

# Loop through the cities and get their latitudes and longitudes using OpenWeatherMap API
df = pd.DataFrame(columns=["City", "Latitude", "Longitude", "Temperature °C"])

def getdata(lat, lon):
    response = requests.get(url2.format(lat, lon, api_key))
    response2 = requests.get(url3.format(lat, lon, api_key))
    data = response.json()
    data2 = response2.json()
    return data, data2


#data, data2 = getdata(14.5, 101.5)
#st.write(data['list'][0]['components']['pm2_5'])
#st.write(data2['name'])
df_air = pd.DataFrame(columns=["City", "Pm2_5"])
#for i in range(len(lat_th)):
#    lat = lat_th[i]
#    st.write(lat)
#    lon = df2.loc[i,['lon']]
#    d1, d2 = getdata(lat, lon)
#    name = d2['name']
#    pm2_5 = d1['list'][0]['components']['pm2_5']
#    df_air = df_air.append({"City": name, "Pm2_5": pm2_5}, ignore_index=True)
st.write(df2.iloc[8, :])
    
for city in cities:    
    # Make the API call and get the response
    response = requests.get(url.format(city, api_key))
    if response:
        data = response.json()
        lat = data["coord"]["lat"]
        lon = data["coord"]["lon"]
        temp_kelvin = data["main"]["temp"]
        temp_celsius = temp_kelvin - 273.15
        
        #st.write(f"Coordinates of {city}: ({lat}, {lon})")
        #st.write(f"Temperature in {city}: {temp_celsius:.1f}°C")
        
        df = df.append({"City": city, "Latitude": lat, "Longitude": lon, "Temperature °C": temp_celsius}, ignore_index=True)
    else:
      st.write(f"Error getting coordinates for {city}")

show_temp = st.beta_expander(label='Current Temperatures')
with show_temp:
    st.table(df[['City', 'Temperature °C']])
  
# Add the heatmap layer to the map
m.add_heatmap(
            df,
            latitude="Latitude",
            longitude="Longitude",
            value="Temperature °C",
            name="Heat map",
            radius=20)

m.to_streamlit(height=700)




