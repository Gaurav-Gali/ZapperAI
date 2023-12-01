import streamlit as st
from dotenv import load_dotenv

# translate
from googletrans import Translator

# ai
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI

# custom modules


class text_processes:
    def get_pdf_text(pdf_docs):
        text = ""

        for pdf in pdf_docs:
            pdf_reader = PdfReader(pdf)
            for page in pdf_reader.pages:
                text += page.extract_text()

        return text

    def get_text_chunks(raw_text):
        text_splitter = CharacterTextSplitter(
            separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len)

        chunks = text_splitter.split_text(raw_text)
        return chunks

    def get_vector_store(text_chunks):
        embeddings = HuggingFaceInstructEmbeddings(
            model_name="hkunlp/instructor-large")
        vectorstore = FAISS.from_texts(
            texts=text_chunks, embedding=embeddings)

        return vectorstore

    def get_conversation_chain(vectorstore):
        llm = ChatOpenAI()
        memory = ConversationBufferMemory(
            memory_key="chat_history", return_messages=True)
        conversation_chain = ConversationalRetrievalChain.from_llm(
            llm=llm, retriever=vectorstore.as_retriever(), memory=memory)

        return conversation_chain


def handle_user_input(user_question):
    response = st.session_state.conversation({"question": user_question})

    st.session_state.chat_history = response['chat_history']

    with st.container():
        for i, message in enumerate(st.session_state.chat_history):
            if i % 2 == 0:
                with st.chat_message(name="ai", avatar="😄"):
                    st.write(message.content)
            else:
                with st.chat_message(name="user", avatar="💬"):
                    st.write(message.content)


st.set_page_config(page_title="Zapper AI", page_icon="💬")


def main():
    load_dotenv()

    disabled = True

    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("Zapper :red[AI] 💬 ")

    pdf_docs = st.file_uploader(
        "\t", accept_multiple_files=True, type=['pdf'])

    if pdf_docs:
        # Translator
        translator = Translator()

        option = st.selectbox(
            "Choose language for conversion", ("Hindi", "Tamil"))

        translated = ""

        raw_text = text_processes.get_pdf_text(pdf_docs)

        b = st.button(f"Translate PDF in {option}")

        if b:
            if option == "Hindi":
                translated = translator.translate(
                    raw_text, src="en", dest="hi")
            elif option == "Tamil":
                translated = translator.translate(
                    raw_text, src="en", dest="ta")
            else:
                translated = "Language not supported !"

            st.download_button("Download Translation", str(translated))

    if pdf_docs:
        disabled = False
    button = st.button("Upload Docs", use_container_width=True,
                       type="primary", disabled=disabled)

    st.divider()

    disabled_input = True

    if button:
        disabled_input = False

    user_question = st.chat_input(
        "Ask Zapper AI about your docs ...")

    if user_question:
        handle_user_input(user_question)

    if button:

        with st.status("Analysing", expanded=True):
            # get pdf text
            raw_text = text_processes.get_pdf_text(pdf_docs)
            # get the text chunks
            text_chunks = text_processes.get_text_chunks(raw_text)
            st.write("Reading")
            # create vector stores
            st.write("Storing")
            vector_store = text_processes.get_vector_store(text_chunks)
            # create conversation chain
            st.session_state.conversation = text_processes.get_conversation_chain(
                vector_store)
            st.write("Ready")


if __name__ == "__main__":
    main()
