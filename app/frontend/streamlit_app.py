import streamlit as st
from app.services.search import SearchService
from app.services.chatbot import build_prompt, generate_answer

st.set_page_config(page_title="Synapsee Test", layout="wide")

st.markdown("<h1 style='text-align: center;'>Chatbot - Synapsee Test</h1>", unsafe_allow_html=True)

st.markdown("""
This chatbot answers questions about cognitive neuroscience, including attention, perception, memory, emotion, and decision-making. Responses are generated using retrieved context from a curated knowledge base. Feel free to ask questions about these topics — the system will provide answers grounded in relevant sources. Enjoy!
""")

# Inicialize once
@st.cache_resource
def load_search():
    return SearchService()

search_service = load_search()

query = st.text_input("Type your question:", placeholder="Ex.: What is the amygdala?")

if query:
    with st.spinner("Searching an answer..."):
        chunks = search_service.search(query, k=5)
        chunks = chunks[:3]

        if not chunks:
            st.warning("Didn't find any relevant information.")
        else:
            prompt = build_prompt(query, chunks)
            answer = generate_answer(prompt)

            st.subheader("Answer")
            st.write(answer)

            st.subheader("Sources")
            for c in chunks:
                with st.expander(f"{c['title']} - {c['section']}"):
                    st.write(c["text"])
                    st.caption(f"Source: {c['source']}")