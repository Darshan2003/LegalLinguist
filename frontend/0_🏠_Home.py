import streamlit as st
from src.Chat import Chat
from src.utils import page_init
import src.pdfops as pdfops
from streamlit_lottie import st_lottie
import requests

page_init()
st.session_state['verif_email'] = 'kenneth@mail.com'


chat = Chat()


def processinput(input: str):
   if input and 'id' in st.session_state.keys():
    uid = st.session_state['id']
    response = requests.get(f"https://api.jugalbandi.ai/query-with-langchain-gpt3-5?query_string={input}&uuid_number={uid}").json()
    chat.message_by_assistant(response['answer'])
    # if input.split(' ')[0] == '/search':
    #     pdfops.search_logic(chat, input)
    # else:
    #     chat.message_by_assistant('Hello how can I help.')


chat.set_processinput(processinput)
if 'show_anim' not in st.session_state:
    st.session_state['show_anim'] = True
    st_lottie("https://lottie.host/4168a67a-474d-4939-a94f-cc090b508bea/gzny9gII5b.json",
              speed=0.8, height=300, key="initial", loop=False)

clearbtn = st.sidebar.button(':broom: Clear Chat')
if clearbtn:
    chat.clear_chat()


clearbtn = st.sidebar.button(':heavy_plus_sign: Create Embedings')
if clearbtn:
    chat.upload_create_embeding()

chat.render_ui()


# * Notes
# doc can be accessed using st.session_state['doc']
# doc is array of uploaded docs
# to add messages use the method 'message_by_assistant(text)'
