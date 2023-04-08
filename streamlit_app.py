import streamlit as st
import leafmap.foliumap as leafmap

import pandas as pd
import requests
import numpy as np

api_key = st.secrets["pass"]


##################################################################
#st.set_page_config(layout="wide")

# Customize page title
st.title("Map")


#map_center = (13.25, 101.5)
m = leafmap.Map(zoom=2,
                draw_control=False,
                measure_control=False,
               )

m.add_tile_layer("http://tile.openweathermap.org/map/temp_new/{z}/{x}/{y}.png?appid={api_key}",
    name="Temperature",
    attribution='&copy; <a href="http://owm.io">VANE</a>')


m.to_streamlit()



