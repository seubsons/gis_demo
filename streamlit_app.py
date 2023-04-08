import streamlit as st
from streamlit_leaflet import st_leaflet
from leafmap import folium as leaf_folium

api_key = st.secrets["pass"]

st.set_page_config(layout="wide")

st.title("Air Quality Map")

m = leaf_folium.Map(location=[60, 50], zoom_start=3)
st_leaflet(m)
