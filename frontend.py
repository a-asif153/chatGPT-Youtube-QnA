import streamlit as st
from backend import comp_process


def frontend():

    st.set_page_config(page_title="Youtube-GPT", layout="wide")
    st.title("Chat with :red[Youtube] Video!")

    question = st.text_input("Ask Question below!", placeholder="Your question here")

    with st.sidebar:
        st.image("img.png")
        api_key = st.text_input("Enter OpenAI apikey below:", placeholder="openai apikey", type="password")
        url = st.text_input("Enter youtube url below:", placeholder="paste url here: ")

    if url and api_key is not None:
        if question:
            ans = comp_process(apikey=api_key, url=url, question=question)
            st.write(ans)


if __name__ == "__main__":
    frontend()