import streamlit as st
import fitz
from src.Chat import Chat
from src.utils import page_init


page_init()


chat = Chat()


def search_and_highlight(doc, text):
    pdf_doc = fitz.open(stream=doc.read(), filetype="pdf")
    found_something = False
    for page in pdf_doc:
        quads = page.search_for(text, quads=True)
        if quads:
            found_something = True
            page.add_highlight_annot(quads)
            chat.message_by_assistant(
                page.get_pixmap().tobytes('png'), type='image')
    if not found_something:
        chat.message_by_assistant("No matches found.")


def processinput(input: str):
    if not input:
        return
    if input.split(' ')[0] == '/search':
        try:
            doc_index = int(input.split(' ')[1]) - 1
            if doc_index >= len(st.session_state['doc']):
                raise ValueError
            # search string
            search_string = ' '.join(input.split(' ')[2:])
            chat.message_by_assistant(
                "Searching for " + search_string + " in file " + str(doc_index + 1))
            search_and_highlight(
                st.session_state['doc'][doc_index], search_string)

        except ValueError:
            chat.message_by_assistant(
                f'You have uploaded only {len(st.session_state["doc"])} files. Please enter a valid index.')
            return


chat.set_processinput(processinput)
chat.render_ui()

# * Notes
# doc can be accessed using st.session_state['doc']
# doc is array of uploaded docs
# to add messages use the method 'message_by_assistant(text)'
