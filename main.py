import streamlit as st
from streamlit_option_menu import  option_menu
from TextQRCodeGenerator import Text
from qr_reader import qr_reader
from WiFiQRCodeGenerator import WiFi
from LocationQRCodeGenerator import Locate
from ContactsQRCodeGenerator import Contacts

selected = option_menu(
    menu_title="Main",
    options=["Text Data", "WiFi", "Location", "Contacts"],
    icons=None,
    menu_icon=None,
    default_index=0,
    orientation="horizontal"
)


if selected == "Text Data":
    with st.container(height=1000):
        file_name = Text.select(selected)
        qr_reader.image(file_name)


if selected == "WiFi":
    with st.container(height=750):
        file_name = WiFi.select(selected)
        qr_reader.image(file_name)

if selected == "Location":
    with st.container(height=750):
        file_name = Locate.select(selected)
        qr_reader.image(file_name)

if selected == "Contacts":
    with st.container(height=820):
        file_name = Contacts.select(selected)
        qr_reader.image(file_name)