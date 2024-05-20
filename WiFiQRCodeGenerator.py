from TextQRCodeGenerator import QRText
import streamlit as st
from segno import helpers

class QRWiFi(QRText):
    def __init__(self, ssid, password, security, file_name, scale):
        self.ssid = ssid
        self.password = password
        self.security = security
        self.file_name = file_name
        self.scale = scale

    @staticmethod
    def qr_code(ssid, password, security, file_name, scale, border, light, dark, **kwargs):
        qrcode = helpers.make_wifi(ssid=ssid, password=password, security=security)
        qrcode.save(f"qr_images/{file_name}.png", scale=scale, border=border, dark=dark, light=light)
        return 0

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

        with col1:
            a_col1, a_col2 = st.columns(2)
            st.markdown("<p style='color: #8A8A8A;'>use colors that don't blend</p>", unsafe_allow_html=True)
            with a_col1:
                light = st.color_picker("Light", "#FFFFFF")
            with a_col2:
                dark = st.color_picker("Dark", "#000000")

        with col2:
            border = st.select_slider(
                "Border",
                options=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                value=2
            )

        QRWiFi.qr_code(ssid=ssid, password=password, security=securety, file_name=file_name, scale=scale, border=border, dark=dark, light=light)
        return file_name



