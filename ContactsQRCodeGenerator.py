from TextQRCodeGenerator import Text
import streamlit as st
from segno import helpers
from qr_reader import qr_reader

class Contacts(Text):

    @staticmethod
    def qr_code(name, email, phone, url, scale, file_name, **kwargs):
        qrcode = helpers.make_vcard(name=name, displayname=name, email=email, phone=phone, url=url)
        qrcode.save(f"qr_images/{file_name}.png", scale=scale)

    @staticmethod
    def select(selected):
        st.markdown(f"<h1 style='text-align: center;'>{selected}</h1>", unsafe_allow_html=True)
        st.divider()

        col1, col2 = st.columns(2)

        with col1:
            name = st.text_input("Name", placeholder="John Doe")
            email = st.text_input("Email", placeholder="me@example.org")

        with col2:
            phone = st.text_input("Phone", placeholder="+1234567")
            url = st.text_input("Website", placeholder="http://www.example.org")

        col1, col2 = st.columns(2)
        with col1:
            file_name = st.text_input("Name file", placeholder="Example qr_code -> qr_code.png")

        with col2:
            scale = st.selectbox(
                "Scale",
                (12, 13, 14, 15, 16, 17, 18, 19, 20)
            )

        Contacts.qr_code(name=name, email=email, phone=phone, url=url, scale=scale, file_name=file_name)
        return file_name
