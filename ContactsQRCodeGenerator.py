from TextQRCodeGenerator import QRText
import streamlit as st
from segno import helpers


class QRContacts(QRText):
    def __init__(self, name, email, phone, url, scale, file_name):
        self.name = name
        self.email = email
        self.phone = phone
        self.url = url
        self.scale = scale
        self.file_name = file_name

    @staticmethod
    def qr_code(name, email, phone, url, scale, file_name, border, light, dark, **kwargs):
        qrcode = helpers.make_vcard(name=name, displayname=name, email=email, phone=phone, url=url)
        qrcode.save(f"qr_images/{file_name}.png", scale=scale, border=border, light=light, dark=dark)
        return 0

    @staticmethod
    def select(selected):
        st.markdown(f"<h1 style='text-align: center;'>{selected}</h1>", unsafe_allow_html=True)
        st.divider()

        col1, col2 = st.columns(2)

        with col1:
            name = st.text_input("Name", placeholder="John Doe")
            email = st.text_input("Email", placeholder="me@example.org")

        with col2:
            phone = st.text_input("Phone", placeholder="+123456789")
            url = st.text_input("Website", placeholder="http://www.example.org")

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

        QRContacts.qr_code(name=name, email=email, phone=phone, url=url, scale=scale, file_name=file_name,
                           border=border, light=light, dark=dark)
        return file_name
