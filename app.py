import streamlit as st; st.title("Hello Kava!")
import pandas as pd
data= {
    "name":["alice","bob","cop"],
    "age" :[34,34,56],
    "city":["new","york","asia"]
}
df = pd.DataFrame(data)
st.title("dataframe")
st.write("here is the thing")
st.title("sidebar example")
income = st.sidebar.number_input("enter your income: " , min_value=2000 , max_value=500000000)
st.sidebar.write(f" you entered : {income}" )
mode = st.sidebar.selectbox("select a mode :" , ["light","drak"])
st.sidebar.write(f"you selected : {mode}")
features = st.sidebar.multiselect("select features :" , ["feature A", "Feature B", "Feature C"])
st.sidebar.write(f"you selected : {features}")

st.dataframe(df)