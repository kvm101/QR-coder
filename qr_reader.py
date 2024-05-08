import streamlit as st
class qr_reader:
    @staticmethod
    def image(file):
        st.markdown("<h1 style='text-align: center;'>QR-CODE</h1>", unsafe_allow_html=True)
        st.divider()

        col1, col2, col3 = st.columns(3)

        with col2:
            st.image(f"qr_images/{file}.png")