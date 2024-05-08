from TextQRCodeGenerator import Text
import streamlit as st
from segno import helpers

class WiFi(Text):

    @staticmethod
    def qr_code(ssid, password, security, file_name, scale, **kwargs):
        qrcode = helpers.make_wifi(ssid=ssid, password=password, security=security)
        qrcode.save(f"qr_images/{file_name}.png", scale=scale)

    @staticmethod
    def select(selected):
        st.markdown(f"<h1 style='text-align: center;'>{selected}</h1>", unsafe_allow_html=True)
        st.divider()

        col1, col2, col3 = st.columns(3)

        with col1:
            ssid = st.text_input("SSID", placeholder="TP-Link")

        with col2:
            password = st.text_input("Password", placeholder="Secret")

        with col3:
            securety = st.selectbox(
                "Security",
                ("WPA", "WPA2", "WPA3", "WEP")
            )

        col1, col2 = st.columns(2)
        with col1:
            file_name = st.text_input("Name file", placeholder="Example qr_code -> qr_code.png")

        with col2:
            scale = st.selectbox(
                "Scale",
                (12, 13, 14, 15, 16, 17, 18, 19, 20)
            )

        WiFi.qr_code(ssid=ssid, password=password, security=securety, file_name=file_name, scale=scale)
        return file_name



