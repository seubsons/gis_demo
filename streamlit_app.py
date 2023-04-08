import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
import requests
import numpy as np

api_key = st.secrets["pass"]


st.set_page_config(layout="wide")

# Customize page title
st.title("Map")


map_center = (13.25, 101.5)
m = leafmap.Map(center=map_center, zoom=6,
                draw_control=False,
                measure_control=False,
               )

col1, col2 = st.columns(2)
with col1:
    m.to_streamlit()
with col2:
    m.to_streamlit()



