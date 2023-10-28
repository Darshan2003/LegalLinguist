import streamlit as st


class Chat():

    def __init__(self, processinput=lambda x: print(x)) -> None:
        self.processinput = processinput
        self.input = None
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
                    st.session_state['doc'] = st.file_uploader(
                        message['text'], accept_multiple_files=True)
                    if st.session_state['doc'] is not None and len(st.session_state['doc']) > 0:
                        with st.spinner("Uploading..."):
                            st.write("Processing the uploaded file...")
                            st.success("Upload and processing complete!")
                elif message['type'] == 'image':
                    st.image(message['image'])

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

    def message_by_assistant(self, message, type='text'):
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
            })
