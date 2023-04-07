import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
import requests
import numpy as np

api_key = st.secrets["pass"]

st.set_page_config(layout="wide")

df2 = pd.read_csv('th.csv')
df3 = df2[0:50]

map_center = (13.25, 101.5)
m = leafmap.Map(center=map_center, zoom=6,
                draw_control=False,
                measure_control=False,
               )

url2 = "http://api.openweathermap.org/data/2.5/air_pollution?lat={}&lon={}&appid={}"

def getdata(lat, lon):
    response = requests.get(url2.format(lat, lon, api_key))
    if response:
        data = response.json()
        pm2_5 = data['list'][0]['components']['pm2_5']
    else:
        pm2_5 = 0.0
    return pm2_5

#### Loop over cities
df3 = df3.assign(pm2_5=[0] * len(df3))
for c in np.arange(len(df3)):
    #st.write(c)
    pm2_5 = getdata(df3.loc[c, 'lat'], df3.loc[c, 'lng'])
    df3.loc[c, 'pm2_5'] = pm2_5
    
######################################################################################################################
# Display Webpage

st.title("Air Quality Map")

col1, col2 = st.columns(2)

# Add the heatmap layer to the map
with col1:
    m.add_heatmap(
                df3,
                latitude="lat",
                longitude="lng",
                value="pm2_5",
                name="PM 2.5",
                radius=25)

    m.to_streamlit(height=700)

with col2:
    show_temp = st.beta_expander(label='PM 2.5')
    with show_temp:
        st.table(df3[['city', 'population', 'pm2_5']])


