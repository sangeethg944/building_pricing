import streamlit as st
from area_estimation.get_image import get_satellite_image
from area_estimation.get_area import PolygonDrawer
from area_estimation.get_contour_area import contour_area


def area_estimation():
    st.markdown("""
            <style>
            .big-font {
                font-size:30px !important;
            }
            </style>
            """, unsafe_allow_html=True)

    st.markdown('<p class="big-font">Area Estimation</p>', unsafe_allow_html=True)

    address = st.text_input('Building Address')

    if st.button('Get Satellite Image'):
        image_requested = get_satellite_image(address)
        st.image(image_requested, caption=address)
        PD = PolygonDrawer("Polygon").run(image_requested)
        contour_image = PD
        area = contour_area(contour_image)
        st.write('Area of the selected region: ', area)
