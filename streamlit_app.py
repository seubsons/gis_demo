import streamlit as st
import leafmap.foliumap as leafmap
from leafmap.markers import Marker
#import leafmap
import requests

api_key = st.secrets["pass"]


st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
Web App URL: <https://template.streamlit.app>
GitHub Repository: <https://github.com/giswqs/streamlit-multipage-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

# Customize page title
#st.title("Streamlit for Geospatial Applications")
st.title("Geospatial Applications")


# st.markdown(
#     """
#     This multipage app template demonstrates various interactive web apps created using [streamlit](https://streamlit.io) and [leafmap](https://leafmap.org). It is an open-source project and you are very welcome to contribute to the [GitHub repository](https://github.com/giswqs/streamlit-multipage-template).
#     """
# )

#st.header("Instructions")

markdown = """
1. For the [GitHub repository](https://github.com/giswqs/streamlit-multipage-template) or [use it as a template](https://github.com/giswqs/streamlit-multipage-template/generate) for your own project.
2. Customize the sidebar by changing the sidebar text and logo in each Python files.
3. Find your favorite emoji from https://emojipedia.org.
4. Add a new app to the `pages/` directory with an emoji in the file name, e.g., `1_🚀_Chart.py`.

"""

#st.markdown(markdown)

#m = leafmap.Map(minimap_control=True)
#m = leafmap.Map(center=(14.5, 101.5))
m = leafmap.Map(height="200px", width="50px",
                draw_control=False,
                measure_control=False,
               )

# Define a list of cities to get temperature data for
cities = ["New York", "Paris", "Tokyo", "Sydney", "Cape Town", "Rio de Janeiro", "Moscow", "Dubai", "Mumbai", "Cairo", "Bangkok"]

url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

# Loop through the cities and get their latitudes and longitudes using OpenWeatherMap API
for city in cities:    
    # Make the API call and get the response
    response = requests.get(url.format(city, api_key))
    if response:
        data = response.json()
        lat = data["coord"]["lat"]
        lon = data["coord"]["lon"]
        temp_kelvin = data["main"]["temp"]
        temp_celsius = temp_kelvin - 273.15
        
        #st.write(f"Coordinates of {city}: ({lat}, {lon})")
        st.write(f"Temperature in {city}: {temp_celsius:.1f}°C")
        
        # Create a Leaflet marker for the city and add it to the map with the temperature as a popup
        marker = Marker(location=[lat, lon], draggable=False)
        marker.bind_popup(f"{city}: {temp_celsius:.1f}°C")
        marker.add_to(m)
    else:
      st.write(f"Error getting coordinates for {city}")

#m.add_basemap("OpenTopoMap")
#m.to_streamlit(height=700)
st.write(m)




