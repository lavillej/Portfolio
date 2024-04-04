import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=300)

with col2:
    st.title("Joshua LaVille")
    content = """
    Hi I'm Joshua, call me Josh. This is just a bunch of random words right now, but eventually this will become my
    first portfolio to show off what I learned in this Python Course.
    """
    st.info(content)