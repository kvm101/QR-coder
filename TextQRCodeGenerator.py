import streamlit as st
import segno as sg

class QRText:
    def __init__(self, content, mask, border, scale, dark, light, boost_error, file_name):
        self.content = content
        self.mask = mask
        self.border = border
        self.scale = scale
        self.dark = dark
        self.light = light
        self.boost_error = boost_error
        self.file_name = file_name

    @staticmethod
    def qr_code(content, mask, border, scale, dark, light, boost_error, file_name):
        qr_code = sg.make_qr(content=content, boost_error=boost_error, mask=mask)
        qr_code.save(f"qr_images/{file_name}.png", border=border, scale=scale, dark=dark, light=light)
        return 0

    @staticmethod
    def select(selected):
            st.markdown(f"<h1 style='text-align: center;'>{selected}</h1>", unsafe_allow_html=True)
            st.divider()
            col1, col2 = st.columns(2)

            with col1:
                text_form = st.radio(
                    "Text Form",
                    ["TextLine", "TextArea"],
                    horizontal=True
                )

                a_col1, a_col2 = st.columns(2)
                st.markdown("<p style='color: #8A8A8A;'>use colors that don't blend</p>", unsafe_allow_html=True)
                with a_col1:
                    light = st.color_picker("Light", "#FFFFFF")
                with a_col2:
                    dark = st.color_picker("Dark", "#000000")

                scale = st.selectbox(
                    "Scale",
                     (12, 13, 14, 15, 16, 17, 18, 19, 20)
                )

                file_name = st.text_input("Name file", placeholder="Example qr_code -> qr_code.png")

            with col2:
                mask = st.select_slider(
                    "Mask",
                    options=[0, 1, 2, 3, 4, 5, 6, 7],
                    value=3
                )

                border = st.select_slider(
                    "Border",
                    options=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                    value=2
                )

                on = st.toggle("Fixer errors")

                if on:
                    boost_error = True
                    st.write("Fixer is on")
                else:
                    boost_error = False
                    st.write("Fixer is off")




            if text_form == "TextLine":
                text = st.text_input("", placeholder="Write Text or URL", max_chars=100)

            if text_form == "TextArea":
                text = st.text_area("", placeholder="Write Text or URL", max_chars=2000, height=200)

            QRText.qr_code(content=text, mask=mask, border=border, scale=scale, dark=dark, light=light, boost_error=boost_error, file_name=file_name)
            return file_name
