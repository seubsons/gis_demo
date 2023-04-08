import streamlit as st
import leafmap
from leafmap import folium


api_key = st.secrets["pass"]


st.set_page_config(layout="wide")

st.title("Air Quality Map")


m = folium.Map(location=[60, 50], zoom_start=3)
m.to_streamlit(height=700)


