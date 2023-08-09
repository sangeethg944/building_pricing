import streamlit as st
from PIL import Image
import numpy as np
import os
from floor_detection.yolo_detection_images import detectObjects


def load_image(image):
    img = Image.open(image)
    img = np.array(img)
    return img


def save_uploaded_file(upload_file):
    with open(os.path.join("floor_detection/temp_img_dir", upload_file.name), "wb") as f:
        f.write(upload_file.getbuffer())
    return st.success("image saved")


def floor_detection():
    st.markdown("""
    <style>
    .big-font {
        font-size:30px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="big-font">Floor Detection</p>', unsafe_allow_html=True)
    image_file = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"])
    if image_file is not None:
        save_uploaded_file(image_file)
        st.image(load_image(image_file), width=512)
        # value = st.slider('Select a value for threshold', 0, 100, 50)
        value = 70

        if value and image_file.name is not None:
            detected_img, floor_count = detectObjects(image_file.name, value)

        st.image(load_image(detected_img), width=512)
        st.write("Number of Floors Detected: ", floor_count)
