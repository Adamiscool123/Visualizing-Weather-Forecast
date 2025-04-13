import streamlit as st
import plotly.express as px
from Backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input('Place: ')
slider = st.slider('Forecast Days', min_value=1, max_value=5,
                   help="Select the number of days.")
Data_view = st.selectbox('Select data to view', ("Temperature", "Sky"))

st.subheader(f'{Data_view} for the next {slider} days in {place}')

try:
    if place:
        filtered = get_data(place, slider)

        if Data_view == "Temperature":
            temp = [dic["main"]["temp"]/10 for dic in filtered]
            d = [dic["dt_txt"] for dic in filtered]
            figure = px.line(x=d, y=temp ,labels={"x" : "Date", "y" : "Temperature(C°)"})
            st.plotly_chart(figure)

        if Data_view == "Sky":
            images = {"Clear": "Imgs/clear.png",
                      "Clouds": "Imgs/cloud.png",
                      "Rain": "Imgs/rain.png",
                      "Snow": "Imgs/snow.png"}
            filte = [dic["weather"][0]["main"] for dic in filtered]
            image_paths = [images[condition] for condition in filte]
            st.image(image_paths, width=115)
except KeyError:
    st.info("You entered a non-existent country please try again")
