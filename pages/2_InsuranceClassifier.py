import streamlit as st

st.set_page_config(page_title="Insurance Classifier", layout="wide")
st.title("Tes")
page = st.sidebar.selectbox("Select a page", ["Data Description", "Prediction", "About Naive Bayes"])
