import streamlit as st
import leafmap.foliumap as leafmap
import folium

import pandas as pd
import requests
import numpy as np
#from folium.plugins import ControlPanel

api_key = st.secrets["pass"]


##################################################################
st.set_page_config(layout="wide")

# Customize page title
st.title("Map")


#map_center = (13.25, 101.5)
# Initialize the map
#m = leafmap.Map(center=[60, 50], zoom=3)
m = leafmap.Map(zoom=2,
                draw_control=False,
                measure_control=False,
               )
#m.add_tile_layer("OSM",name='osm',attribution='att')
# m.add_tile_layer(
#     "MODIS",
#     url="http://{s}.sat.owm.io/sql/{z}/{x}/{y}?select=b1,b4,b3&from=modis&order=last&color=modis&appid=d22d9a6a3ff2aa523d5917bbccc89211",
#     name='modis',
#     attribution='&copy; <a href="http://owm.io">VANE</a>',
# )

# temp = leafmap.TileLayer(
#     "http://tile.openweathermap.org/map/temp_new/{z}/{x}/{y}.png?appid={api_key}",
#     attribution='&copy; <a href="http://owm.io">VANE</a>',
#     id="temp",
# )
# m.add_layer(temp)

m.to_streamlit()



