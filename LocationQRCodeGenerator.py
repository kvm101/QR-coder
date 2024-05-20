from TextQRCodeGenerator import QRText
import streamlit as st
import segno


class QRLocate(QRText):
    def __init__(self, latitude, longitude, scale, file_name, content, mask, border, dark, light, boost_error):
        super().__init__(content, mask, border, scale, dark, light, boost_error, file_name)
        self.latitude = latitude
        self.longitude = longitude
        self.scale = scale
        self.file_name = file_name

    @staticmethod
    def qr_code(latitude, longitude, scale, file_name, border, light, dark, **kwargs):
        location_str = f"geo:{latitude},{longitude}"
        qr = segno.make(location_str)
        qr.save(f'qr_images/{file_name}.png', scale=scale, border=border, light=light, dark=dark)
        return file_name

    @staticmethod
    def select(selected):
        st.markdown(f"<h1 style='text-align: center;'>{selected}</h1>", unsafe_allow_html=True)
        st.divider()

        col1, col2 = st.columns(2)
        with col1:
            latitude = st.text_input("Latitude", 0, placeholder="0.00000")

            try:
                latitude = float(latitude)
            except ValueError:
                st.markdown("<p style='color:red;'>input is not a number!</p>", unsafe_allow_html=True)

        with col2:
            longitude = st.text_input("Longitude", 0, placeholder="0.00000")

            try:
                longitude = float(longitude)
            except ValueError:
                st.markdown("<p style='color:red;'>input is not a number!</p>", unsafe_allow_html=True)

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

        QRLocate.qr_code(latitude, longitude, scale, file_name, border, dark=dark, light=light)
        return file_name
