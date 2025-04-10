import streamlit as st
import pandas as pd


st.title("Weather Forecast for the Next Days")
place = st.text_input('Place: ')
slider = st.slider('Forecast Days', min_value=1, max_value=5,
                   help="Select the number of days.")
Data_view =  st.selectbox('Select data to view', ("Temperature", "Sky"))
st.subheader(f'{Data_view} for the next {slider} days in {place}')


