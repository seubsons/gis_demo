import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
import requests
import numpy as np
#from folium.plugins import ControlPanel

api_key = st.secrets["pass"]


# Define layers
providers = {}

providers["OSM"] = {
    "title": "OSM",
    "icon": "img/layers-osm.png",
    "layer": leafmap.builtin_layers["OpenStreetMap"]
}

providers["Satellite"] = {
    "title": "MODIS",
    "icon": "img/layers-satellite.png",
    "layer": leafmap.add_tile_layer(
        url="http://{s}.sat.owm.io/sql/{z}/{x}/{y}?select=b1,b4,b3&from=modis&order=last&color=modis&appid=d22d9a6a3ff2aa523d5917bbccc89211",
        attribution='<a href="http://owm.io">VANE</a>',
        max_zoom=19
    )
}

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

m.to_streamlit()



