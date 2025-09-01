import streamlit as st
from langchain_deepseek import ChatDeepSeek
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
load_dotenv()


st.title("Briefly")

def generate_response(user_input):
    llm = ChatDeepSeek(
        model="deepseek-chat",
        temperature=0,
        max_tokens=50,
        timeout=None,
        max_retries=0,
        api_key=os.getenv("DEEPSEEK_API_KEY")

    )
    
    prompt = ChatPromptTemplate.from_template(
        "You are a concise summarizer. Summarize the following text in 5-8 bullet points:\n{input_text}"
    )

    chain = prompt | llm
    response = chain.invoke(
        {
            "input_text": f"{user_input}"
        }
    )
    return response.content

with st.form("summarize"):
    text = st.text_area(
        "Enter text to summarize",
        "",
    )
    submitted = st.form_submit_button("Summarize")
    if submitted:
        message = generate_response(text)
        st.info(message)
