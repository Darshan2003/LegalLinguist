import streamlit as st


class Chat():
    doc = None

    def __init__(self) -> None:
        if 'doc' not in st.session_state:
            st.session_state['doc'] = None

        if 'messages' not in st.session_state:
            st.session_state['messages'] = []
            self.message_by_assistant(
                'Hello there! I am your personal assistant. How can I help you?')
            self.message_by_assistant('Upload your file here:', type='file')

    def render_ui(self):
        self.handle_input()
        for message in st.session_state['messages']:
            with st.chat_message(message['role']):
                if message['type'] == 'text':
                    st.write(message['text'])
                elif message['type'] == 'file':
                    st.session_state['doc'] = st.file_uploader(message['text'])
                    if st.session_state['doc'] is not None:
                        with st.spinner("Uploading..."):
                            st.write("Processing the uploaded file...")
                            st.success("Upload and processing complete!")

    def handle_input(self):
        input = st.chat_input('Type a message...')
        if input and st.session_state['doc'] == None:
            st.session_state['messages'].append({
                'type': 'text',
                'text': input,
                'role': 'user',
            })
            st.session_state['messages'].append({
                'type': 'text',
                'text': 'Please upload your file first.',
                'role': 'assistant',
            })
        elif input:
            st.session_state['messages'].append({
                'type': 'text',
                'text': input,
                'role': 'user',
            })
            st.session_state['messages'].append({
                'type': 'text',
                'text': 'Hello there! I am your personal assistant. How can I help you?',
                'role': 'assistant',
            })

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
