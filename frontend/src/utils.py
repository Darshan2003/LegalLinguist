import streamlit as st


def page_init():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-repeat: no-repeat;
                padding-top: 10px;
                background-position: 20px 20px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "Law Query";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 80px;
                border-bottom: 1px solid #d0d0d0;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
