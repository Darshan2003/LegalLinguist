import streamlit as st


def page_init():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"]::before {
                content: "Legal Linguist";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 80px;
                font-weight: bold;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    # st.sidebar.markdown("# Legal Linguist")
