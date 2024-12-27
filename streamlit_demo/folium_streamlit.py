import streamlit as st
import folium
from streamlit_folium import st_folium


st.set_page_config(page_title="GeoJSON Visualization", layout="wide")

# geoJSON static url here 
geojson_url = "http://localhost:8000/cbsa.geojson"

# Create a folium map
m = folium.Map(location=[37.7749, -122.4194], zoom_start=5)

# Add the GeoJSON layer
folium.GeoJson(
    geojson_url,  # Fetches the GeoJSON from the server
    name="geojson",
    tooltip=folium.GeoJsonTooltip(fields=["NAME", "GEOID"], aliases=["Name:", "GEOID:"]),
).add_to(m)

# Add a layer control panel -- necessary ?
folium.LayerControl().add_to(m)

# dispalying map
st.title("GeoJSON Visualization")
st_data = st_folium(m, width=800, height=600)
