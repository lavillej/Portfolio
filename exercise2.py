import streamlit as st
import pandas

st.set_page_config(layout="wide")

header1 = "**The Best Company**"
intro = """
Lorem ipsum dolor sit amet, ne duo error moderatius, in mel volutpat reprimique. Sea aliquid consequuntur cu, esse 
minimum luptatum per ex. Labitur denique suscipiantur per an, eirmod civibus ius et. Rebum consulatu qui eu. Viris 
ponderum sed te, dicunt albucius vix ei, pro congue putent ea. Modus nostrud iuvaret sea eu, mea te elit erat.
"""
subheader1 = "Our Team"

st.header(header1)
st.write(intro)
st.subheader(subheader1)

col1, col2, col3 = st.columns(3)

df = pandas.read_csv("exercise_resources/data_bonus.csv")

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("exercise_resources/images/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("exercise_resources/images/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("exercise_resources/images/" + row["image"])