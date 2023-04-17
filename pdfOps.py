import base64
import streamlit as st


def show_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1600" height="1200" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)
