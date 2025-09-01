import streamlit as st

st.title("Briefly")

def generate_response(input_text):
    st.info(input_text)


with st.form("summarize"):
    text = st.text_area(
        "Enter text to summarize - word limit 10,000",
        "",
    )
    submitted = st.form_submit_button("Summarize")
    if submitted:
        generate_response(text)
