import streamlit as st
from streamlit_option_menu import option_menu
from TextQRCodeGenerator import QRText
from qr_reader import qr_reader
from WiFiQRCodeGenerator import QRWiFi
from LocationQRCodeGenerator import QRLocate
from ContactsQRCodeGenerator import QRContacts

st.set_page_config(
        page_title="QR-CODER",
        page_icon="images/favicon.png",
        layout="centered" or "wide",
        initial_sidebar_state="auto",
    )

def main():
    # Вибір опцій з використанням option_menu
    selected = option_menu(
        menu_title="QR-CODER",
        options=["Text Data", "WiFi", "Location", "Contacts"],
        icons=["cursor-text", "wifi", "map", "person-lines-fill"],
        menu_icon="qr-code",
        default_index=0,
        orientation="horizontal"
    )

    # Показати відповідний інтерфейс залежно від вибору користувача
    if selected == "Text Data":
        # Виклик методу вибору текстових даних і відображення зображення QR-коду
        with st.container(height=1100):
            file_name = QRText.select(selected)
            qr_reader.image(file_name)

    if selected == "WiFi":
        # Виклик методу вибору даних WiFi і відображення зображення QR-коду
        with st.container(height=950):
            file_name = QRWiFi.select(selected)
            qr_reader.image(file_name)

    if selected == "Location":
        # Виклик методу вибору геолокаційних даних і відображення зображення QR-коду
        with st.container(height=960):
            file_name = QRLocate.select(selected)
            qr_reader.image(file_name)

    if selected == "Contacts":
        # Виклик методу вибору контактних даних і відображення зображення QR-коду
        with st.container(height=1020):
            file_name = QRContacts.select(selected)
            qr_reader.image(file_name)

if __name__ == "__main__":
    main()