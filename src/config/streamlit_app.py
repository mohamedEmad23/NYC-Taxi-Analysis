import pandas as pd
import streamlit as st
import pygwalker as pyg
from pygwalker.api.streamlit import StreamlitRenderer

st.set_page_config(page_title="Taxi Explorer", layout="wide")
st.title("NYC Taxi Data Explorer")

@st.cache_data
def load_data():
    return pd.read_csv("/root/DevDataOps/Datasets/taxi_analysis/taxi_trip_data.csv")

df = load_data()
renderer = StreamlitRenderer(
    df,
    spec="./gw_config.json",
    spec_io_mode="rw",
    kernel_computation=True
)
renderer.explorer()