import streamlit as st
from PIL import Image
from floor_detection.floor_app import floor_detection
from area_estimation.area_app import area_estimation


st.title("Building Pricing Model")
# image = Image.open(r"C:\Users\91974\PycharmProjects\Building Pricing Model\Allianz.png")
image = Image.open(r"Allianz.png")
st.sidebar.image(image)

st.sidebar.header("Approaches")
choice = st.sidebar.selectbox("Tasks", ["Floor Detection", "Area Estimation"])
if choice == "Floor Detection":
    floor_detection()
if choice == "Area Estimation":
    area_estimation()
