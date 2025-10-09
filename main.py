import streamlit as st
import plotly.express as px
from backend import get_data

#express is module, plotly is library
#Add titile, text input ,slider,selectionbox and subheader
st.title("Weather Forcast for Next Days ")
place = st.text_input("Place")

days = st.slider("Forcast Days",min_value=1,max_value=5,
               help="select number of forecasted days")
option = st.selectbox("select data to view",
                      ("Temperature","Sky"))
st.subheader(f"{option} for next {days} days in {place}")
if place:
#get the temperature/sky day
    filtered_data = get_data(place,days)
    #print(filtered_data)
    if option == "Temperature":
    #create a temperature plot
        temperatures = [dict['main']['temp'] /10  for dict in filtered_data]; print("temp=",temperatures)
        dates = [dict['dt_txt'] for dict in filtered_data];print(dates)
        figure = px.line(x=dates , y=temperatures  ,labels={"x": "Date","y":"Temperaturs(C)"})
        st.plotly_chart(figure)
        #plotly_chart() is a method responsible to create a graph
        # and this method now gets a figure object as input
        #figure object you can get it from plotting library,from a data visualization library
        #plotly is data visualization library, such as plotly orBokeh
    if  option == "Sky":
        img_dic = {'Clear': "images/clear.png", 'Cloud': "images/cloud.png", 'Rain': "images/rain.png",
                   'Snow': "images/snow.png"}
        sky_conditions= [dict['weather'][0]['main'] for dict in filtered_data]
        image_path=[img_dic[condition] for condition in sky_conditions]
        print(sky_conditions)
        st.image(image_path,width=115)