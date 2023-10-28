import streamlit as st
from src.Chat import Chat
from src.utils import page_init
import src.pdfops as pdfops

page_init()


chat = Chat()


def processinput(input: str):
    if not input or st.session_state['doc'] is None or len(st.session_state['doc']) == 0:
        return
    if input.split(' ')[0] == '/search':
        pdfops.search_logic(chat, input)


chat.set_processinput(processinput)
chat.render_ui()

# * Notes
# doc can be accessed using st.session_state['doc']
# doc is array of uploaded docs
# to add messages use the method 'message_by_assistant(text)'
