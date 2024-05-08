from TextQRCodeGenerator import Text
import streamlit as st
import segno
from segno import helpers

class Locate(Text):
    @staticmethod
    def qr_code(latitude, longitude, scale, file_name, **kwargs):
        location_str = f"geo:{latitude},{longitude}"
        qr = segno.make(location_str)
        qr.save(f'qr_images/{file_name}.png', scale=scale)

    @staticmethod
    def select(selected):
        st.markdown(f"<h1 style='text-align: center;'>{selected}</h1>", unsafe_allow_html=True)
        st.divider()

        col1, col2 = st.columns(2)
        with col1:
            latitude = st.text_input("Latitude", placeholder="0.00000")

        with col2:
            longitude = st.text_input("Longitude", placeholder="0.00000")

        col1, col2 = st.columns(2)
        with col1:
            file_name = st.text_input("Name file", placeholder="Example qr_code -> qr_code.png")

        with col2:
            scale = st.selectbox(
                "Scale",
                (12, 13, 14, 15, 16, 17, 18, 19, 20)
            )

        Locate.qr_code(latitude, longitude, scale, file_name)
        return file_name
