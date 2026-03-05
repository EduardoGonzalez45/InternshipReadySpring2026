import datetime

import streamlit as st
import pandas as pd
import plotly_express as px
from APIs import apod_generator
import os
from dotenv import load_dotenv


# In the terminal, run streamlit run dashboard.py
st.title("Water Quality Dashboard")
st.header("Internship Ready Software Development")
st.subheader("Eduardo Gonzalez")
st.divider()

df = pd.read_csv("biscayneBay_waterquality.csv")

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["Descriptive Statistics",
     "2d Plots",
     "3d Plots",
     "NASA's Astronomy Picture of the Day",
     "Example Graph"]
)

water_data = {
    "temperature":[78, 80, 85, 86, 87, 89, 92],
    "ph":[6.5, 6.7, 6.3, 6.2, 6.6, 7.1, 7.2],
    "oxygen":[7.2, 5.6, 3.5, 4.1, 4.5, 7.4, 6.7]
}

df_water = pd.DataFrame(water_data)

with tab1:
    st.info("Working on this")
    st.dataframe(df)
    st.caption("Raw Data")
    st.divider()
    st.dataframe(df.describe())
    st.caption("Descriptive Statistics")

with tab2:
    fig1 = px.line(df,
                   x="Time",
                   y="Temperature (c)")
    st.plotly_chart(fig1)

    fig2 = px.scatter(df,
                      x="ODO mg/L",
                      y="Temperature (c)",
                      color="pH")

with tab3:

    fig3 = px.scatter_3d(df,
                         x="Longitude",
                         y="Latitude",
                         z="Total Water Column (m)",
                         color="Temperature (c)")
    fig3.update_scenes(zaxis_autorange="reversed")
    st.plotly_chart(fig3)

with tab4:
    st.header("NASA's Astronomy Picture of the Day")
    st.title(apod_generator(url, unique_key)["title"])

with tab5:
    st.dataframe(df_water)