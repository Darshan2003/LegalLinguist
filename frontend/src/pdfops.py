import streamlit as st
import fitz


def search_and_highlight(chat, doc, text):
    pdf_doc = fitz.open(stream=doc.read(), filetype="pdf")
    found_something = False
    for page in pdf_doc:
        quads = page.search_for(text, quads=True)
        if quads:
            found_something = True
            page.add_highlight_annot(quads)
            chat.message_by_assistant(
                page.get_pixmap().tobytes('png'), type='image', label="Found " + str(len(quads)) +
                " matches in page " + str(page.number + 1) + ".")
    if not found_something:
        chat.message_by_assistant("No matches found.")


def search_logic(chat, input):
    try:
        doc_index = int(input.split(' ')[1]) - 1
        if doc_index >= len(st.session_state['doc']):
            raise ValueError

        # search string
        search_string = ' '.join(input.split(' ')[2:])
        chat.message_by_assistant(
            "Searching for " + search_string + " in file " + str(doc_index + 1))
        search_and_highlight(chat,
                             st.session_state['doc'][doc_index], search_string)

    except ValueError:
        chat.message_by_assistant(
            f'You have uploaded only {len(st.session_state["doc"])} files. Please enter a valid index.')
        return
