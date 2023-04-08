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

##################################################################
st.set_page_config(layout="wide")

# Customize page title
st.title("Map")

#st.write(data)

map_center = (13.25, 101.5)
m = leafmap.Map(center=map_center, zoom=6,
                draw_control=False,
                measure_control=False,
               )

#m.add_basemap("Esri.WorldImagery")
# Esri.NatGeoWorldMap
# Esri.OceanBasemap
# Esri.WorldGrayCanvas
#m.add_basemap("Esri.WorldImagery")
# Esri.WorldPhysical
# Esri.WorldShadedRelief
m.add_basemap("HYBRID")
m.add_basemap("Esri.WorldStreetMap")
# Esri.WorldTerrain
#m.add_basemap("Esri.WorldTopoMap")
#m.add_basemap("Strava.All")

# m.add_tile_layer(url="https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}",
#         attribution="Google",
#         name="Google Satellite",
#                 )


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


