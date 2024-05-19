import streamlit as st
class qr_reader:
    @staticmethod
    def image(file):
        st.markdown("<h1 style='text-align: center;'>QR-CODE</h1>", unsafe_allow_html=True)
        st.divider()

        col1, col2, col3 = st.columns(3)

        with col2:
            st.image(f"qr_images/{file}.png")

            with open(f"qr_images/{file}.png", "rb") as data:
                btn = st.download_button(
                    label="Download image",
                    data=data,
                    file_name=f"{file}.png",
                    mime="image/png",
                    use_container_width=True
                )
        return file