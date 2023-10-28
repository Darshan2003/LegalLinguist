import streamlit as st
import requests
import base64
import time


class Chat():

    def __init__(self, processinput=lambda x: print(x)) -> None:
        self.processinput = processinput
        self.input = None
        self.URL = 'https://c1e0-34-34-36-126.ngrok-free.app'

        if 'doc' not in st.session_state:
            st.session_state['doc'] = None

        if 'messages' not in st.session_state:
            st.session_state['messages'] = []
            self.message_by_assistant(
                'Hello there! I am your personal assistant. How can I help you?')
            self.message_by_assistant('Upload your file here:', type='file')

    def set_processinput(self, processinput):
        self.processinput = processinput

    def render_ui(self):
        self.handle_input()

        for message in st.session_state['messages']:
            with st.chat_message(message['role']):
                if message['type'] == 'text':
                    st.write(message['text'])

                elif message['type'] == 'file':
                    uploaded_files = st.file_uploader(
                        message['text'], accept_multiple_files=True)
                    if uploaded_files is not None and len(uploaded_files) > 0:
                        with st.spinner("Uploading and processing the file..."):
                            self.upload_file()
                            st.success("File processing complete!")

                elif message['type'] == 'image':
                    if message['label'] != '':
                        with st.expander(message['label']):
                            st.image(message['image'])
                    else:
                        st.image(message['image'])

    def upload_file(self):
        # single_file = st.session_state['doc'][index]
        if st.session_state['doc'] is None or len(st.session_state['doc']) == 0:
            return

        single_file = st.session_state['doc'][0]
        print(single_file)
        if not single_file or single_file == None:
            st.write("File not selected")
            return

        response = requests.post(
            f'{self.URL}/uploadfiles',
            files={
                'files': (single_file.name, single_file.read())
            },
            data={
                'email': st.session_state['verif_email']
            }
        )
        result = response.json()
        if result['SUCCESS'] == 'PDF CREATED':
            st.session_state[
                'doc_link'] = f'https://railrakshak.s3.ap-south-1.amazonaws.com/{st.session_state["verif_email"]}{single_file.name}'
            st.write(st.session_state['doc_link'])
            doc = requests.get(st.session_state['doc_link'], stream=True).raw
            pdf_display = F'<iframe src="{st.session_state["doc_link"]}" width="700" height="1000" type="application/pdf"></iframe>'
        # # print(response.json())
        # if response.status_code == 200:
        #     st.write("You've successfully uploaded a file!")
        # else:
        #     st.write("Failed to upload file.")

    def handle_input(self):
        self.input = st.chat_input('Type a message...')
        if self.input and len(st.session_state['doc']) == 0:
            st.session_state['messages'].append({
                'type': 'text',
                'text': self.input,
                'role': 'user',
            })
            st.session_state['messages'].append({
                'type': 'text',
                'text': 'Please upload your file first.',
                'role': 'assistant',
            })
        elif self.input:
            st.session_state['messages'].append({
                'type': 'text',
                'text': self.input,
                'role': 'user',
            })
        self.processinput(self.input)

    def message_by_user(self, message):
        st.session_state['messages'].append({
            'type': 'text',
            'text': message,
            'role': 'user',
        })

    def message_by_assistant(self, message, type='text', label=''):
        if type == 'file':
            st.session_state['messages'].append({
                'type': 'file',
                'text': message,
                'role': 'assistant',
            })
        elif type == 'text':
            st.session_state['messages'].append({
                'type': 'text',
                'text': message,
                'role': 'assistant',
            })
        elif type == 'image':
            st.session_state['messages'].append({
                'type': 'image',
                'image': message,
                'role': 'assistant',
                'label': label
            })

    def clear_chat(self):
        st.session_state['messages'] = []
        st.session_state['doc'] = None
        del st.session_state['show_anim']
        self.message_by_assistant(
            'Hello there! I am your personal assistant. How can I help you?')
        self.message_by_assistant('Upload your file here:', type='file')


# pdf = requests.get(
#     'https://railrakshak.s3.ap-south-1.amazonaws.com/AFFAIRE+C.P.+ET+M.N.+c.+FRANCE.pdf').content
# pdf_base64 = base64.b64encode(pdf).decode('utf-8')
# st.markdown(
#     F'<iframe src="data:application/pdf;base64,{pdf_base64}" width="700" height="1000" type="application/pdf"></iframe>', unsafe_allow_html=True)
