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
st.write(df2.head())

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

# Loop through the cities and get their latitudes and longitudes using OpenWeatherMap API
df = pd.DataFrame(columns=["City", "Latitude", "Longitude", "Temperature °C"])

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




