import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
import requests
import numpy as np

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


df2 = pd.read_csv('th.csv')
#st.write(len(df2))
df3 = df2[0:50]
#st.write(df3)
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
#m = leafmap.Map(center=(14.5, 101.5), height="200px", width="50px")
map_center = (13.25, 101.5)
m = leafmap.Map(center=map_center, zoom=6,
                draw_control=False,
                measure_control=False,
               )

# Define a list of cities to get temperature data for
cities = ["New York", "Paris", "Tokyo", "Sydney", "Cape Town", "Rio de Janeiro", "Moscow", "Dubai", "Mumbai", "Cairo", "Bangkok"]

url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
url2 = "http://api.openweathermap.org/data/2.5/air_pollution?lat={}&lon={}&appid={}"
#url3 = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}"

# Loop through the cities and get their latitudes and longitudes using OpenWeatherMap API
df = pd.DataFrame(columns=["City", "Latitude", "Longitude", "Temperature °C"])

def getdata(lat, lon):
    response = requests.get(url2.format(lat, lon, api_key))
    if response:
    #response2 = requests.get(url3.format(lat, lon, api_key))
        data = response.json()
        pm2_5 = data['list'][0]['components']['pm2_5']
    #data2 = response2.json()
    else:
        pm2_5 = 0.0
    return pm2_5

#### Loop over cities
# df3 = df3.assign(pm2_5=[0] * len(df3))
# for c in np.arange(len(df3)):
#     #st.write(c)
#     pm2_5 = getdata(df3.loc[c, 'lat'], df3.loc[c, 'lng'])
#     df3.loc[c, 'pm2_5'] = pm2_5
#st.write(df3)
    
#for city in cities:
#    # Make the API call and get the response
#    response = requests.get(url.format(city, api_key))
#    if response:
#        data = response.json()
#        lat = data["coord"]["lat"]
#        lon = data["coord"]["lon"]
#        temp_kelvin = data["main"]["temp"]
#        temp_celsius = temp_kelvin - 273.15
#
#        #st.write(f"Coordinates of {city}: ({lat}, {lon})")
#        #st.write(f"Temperature in {city}: {temp_celsius:.1f}°C")
#
#        df = df.append({"City": city, "Latitude": lat, "Longitude": lon, "Temperature °C": temp_celsius}, ignore_index=True)
#    else:
#      st.write(f"Error getting coordinates for {city}")

######################################################################################################################
# Customize page title
st.title("Air Quality Map")

col1, col2 = st.columns(2)
#show_temp = st.beta_expander(label='Current Temperatures')
#with show_temp:
#    st.table(df[['City', 'Temperature °C']])
with col2:
    layer = "precipitation_new"
    #url_map = "https://tile.openweathermap.org/map/{layer}/6/10/10.png?appid={api_key}"
    url_map = "https://tile.openweathermap.org/map/{layer}/{z}/{x}/{y}.png?appid={api_key}"
    #m.add_tile_layer(url=url_map, name="Precipitation")
    m.add_tile_layer(url=url_map, name="Precipitation", attribution="Map data © OpenWeatherMap")
    m.add_layer_control()
    #m.add_basemap(url_map)
    #m.add_layer_control()
    #m.set_center(0, 0, 2)
    m.to_streamlit(height=700)
#     show_temp = st.beta_expander(label='PM 2.5')
#     with show_temp:
#         st.table(df3[['city', 'population', 'pm2_5']])

# Add the heatmap layer to the map
#m.add_heatmap(
#            df,
#            latitude="Latitude",
#            longitude="Longitude",
#            value="Temperature °C",
#            name="Heat map",
#            radius=20)

with col1:
#     m.add_heatmap(
#                 df3,
#                 latitude="lat",
#                 longitude="lng",
#                 value="pm2_5",
#                 name="PM 2.5",
#                 radius=25)

    m.to_streamlit(height=700)




