import streamlit as st

st.title("Weather Forcast for Next Days ")
place=st.text_input("Place")
days=st.slider("Forcast Days",min_value=1,max_value=5,
               help="select number of forecasted days")
option = st.selectbox("select data to view",
                      ("Temperature","Sky"))
st.subheader(f"{option} for next {days} days in {place}")

