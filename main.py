import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Weather Forecast for the Next Days")
place = st.text_input('Place: ')
slider = st.slider('Forecast Days', min_value=1, max_value=5,
                   help="Select the number of days.")
Data_view =  st.selectbox('Select data to view', ("Temperature", "Sky"))
st.subheader(f'{Data_view} for the next {slider} days in {place}')

def get_data(days):
    Dates = ["Sep 30, 2022", "Oct 1, 2022", "Oct 2, 2022"]
    Temperatures = [10,11,15]
    Temperatures = [slider * i for i in Temperatures]
    return Dates, Temperatures

d, t = get_data(slider)

figure = px.line(x=d, y=t ,labels={"x" : "Date", "y" : "Temperature(C°)"})
st.plotly_chart(figure)


