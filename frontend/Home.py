import streamlit as st
from src.Chat import Chat


chat = Chat()
chat.render_ui()

# * Notes
# doc can be accessed using st.session_state['doc']
# right now only one doc is being uploaded and maintained
# to add messages use the method 'message_by_assistant(text)'
