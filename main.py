from pkgutil import get_data

import streamlit as st
import plotly.express as px

#express is module, plotly is library

st.title("Weather Forcast for Next Days ")
place = st.text_input("Place")

days = st.slider("Forcast Days",min_value=1,max_value=5,
               help="select number of forecasted days")
print("days=" + str(days))
option = st.selectbox("select data to view",
                      ("Temperature","Sky"))
st.subheader(f"{option} for next {days} days in {place}")

def get_Data(days):
    dates=['2022-25-10','2022-26-10','2022-27-10']
    tempratures=[10,11,15]
    tempratures=[days * i for i in tempratures]
    return dates,tempratures
#figure object

d, t=get_data(days)

figure = px.line(x=d , y=t  ,labels={"x": "Date","y":"Tempraturs(C)"})
st.plotly_chart(figure)
#plotly_chart() is a method responsible to create a graph
# and this method now gets a figure object as input
#figure object you can get it from plotting library,from a data visualization library
#plotly is data visualization library, such as plotly orBokeh