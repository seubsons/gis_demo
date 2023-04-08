import streamlit as st
import leafmap.foliumap as leafmap

import pandas as pd
import requests
import numpy as np

api_key = st.secrets["pass"]

# city = 'bangkok'
# url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
# response = requests.get(url.format(city, api_key))
# data = response.json()
#st.write(data)


df2 = pd.read_csv('th.csv')
df3 = df2[0:50]

map_center = (13.25, 101.0)

url2 = "http://api.openweathermap.org/data/2.5/air_pollution?lat={}&lon={}&appid={}"
def getdata(lat, lon):
    response = requests.get(url2.format(lat, lon, api_key))
    if response:
        data = response.json()
        pm2_5 = data['list'][0]['components']['pm2_5']
    else:
        pm2_5 = 0.0
        data = 0.0
    return pm2_5, data

df3 = df3.assign(pm2_5=[0] * len(df3))
c = 0
pm2_5, data = getdata(df3.loc[c, 'lat'], df3.loc[c, 'lng'])
df3.loc[c, 'pm2_5'] = pm2_5

##################################################################
st.set_page_config(layout="wide")
st.write(data)

# Customize page title
st.title("OpenWeather leafmap")

# //////////////////////////////////////
st.header("PM2.5")
st.write("Last Updated: ")
col1, col2 = st.columns(2)
with col1:
    m = leafmap.Map(center=map_center, zoom=6,
                draw_control=False,
                measure_control=False,
               )
    m.add_heatmap(
                df3,
                latitude="lat",
                longitude="lng",
                value="population",
                name="Heatmap",
                radius=25)
    m.to_streamlit(height=700)

with col2:
    show_temp = st.beta_expander(label='PM2.5')
    with show_temp:
        st.table(df3[['city', 'population', 'pm2_5']])

# //////////////////////////////////////
st.header("Weather")

m = leafmap.Map(center=map_center, zoom=8,
                draw_control=False,
                measure_control=False,
               )

m.add_basemap("HYBRID", show=False)
m.add_basemap("Esri.WorldStreetMap", show=True)

layer = "precipitation_new"
m.add_tile_layer(url=f"http://tile.openweathermap.org/map/{layer}/{{z}}/{{x}}/{{y}}.png?appid={api_key}",
        attribution="OWM",
        name="Precipitation",
                )
layer = "clouds_new"
m.add_tile_layer(url=f"http://tile.openweathermap.org/map/{layer}/{{z}}/{{x}}/{{y}}.png?appid={api_key}",
        attribution="OWM",
        name="Clouds",
        shown=False,
                )
layer = "pressure_new"
m.add_tile_layer(url=f"http://tile.openweathermap.org/map/{layer}/{{z}}/{{x}}/{{y}}.png?appid={api_key}",
        attribution="OWM",
        name="Pressure",
        shown=False,
        opacity=1.0,
                )
layer = "wind_new"
m.add_tile_layer(url=f"http://tile.openweathermap.org/map/{layer}/{{z}}/{{x}}/{{y}}.png?appid={api_key}",
        attribution="OWM",
        name="Wind",
        shown=False,
        opacity=1.0,
                )
layer = "temp_new"
m.add_tile_layer(url=f"http://tile.openweathermap.org/map/{layer}/{{z}}/{{x}}/{{y}}.png?appid={api_key}",
        attribution="OWM",
        name="Tempurature",
        shown=False,
        opacity=1.0,
                )

m.to_streamlit(height=700)


