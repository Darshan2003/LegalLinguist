import streamlit as st
import base64
from src.utils import page_init

page_init()
st.markdown("# Manage Documents")

with st.expander("## sample.pdf"):
    
    
    with open('sample.pdf', "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="100%" height="1000" type="application/pdf">'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)

st.button("Clear All")