import streamlit as st
import pydeck as pdk
import json


st.set_page_config(page_title="MSA GeoJSON Visualization", layout="wide")

@st.cache_data  
def load_geojson(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def main():

    st.title("MSA GeoJSON Visualization")

    geojson_path = "../tl_2024_us_cbsa/cbsa.geojson"
    geojson_data = load_geojson(geojson_path)

    geojson_layer = pdk.Layer(
        "GeoJsonLayer",
        geojson_data,
        get_fill_color="[200, 30, 0, 160]",
        get_line_color="[255, 255, 255]",
        pickable=True,
    )

    initial_view_state = pdk.ViewState(
        latitude=37.7749,
        longitude=-122.4194,
        zoom=4,
        pitch=0,
    )

    st.pydeck_chart(
        pdk.Deck(
            layers=[geojson_layer],
            initial_view_state=initial_view_state,
            map_style="mapbox://styles/mapbox/streets-v11",
        )
    )


if __name__ == "__main__":
    main()
