import streamlit as st

st.title("Briefly")

def generate_response(input_text):
    st.info("""hello""")


with st.form("summarize"):
    text = st.text_area(
        "Enter text to summarize - word limit 10,000",
        """Elon Reeve Musk FRS (/lɒn/ EE-lon; born June 28, 1971) is an international businessman and entrepreneur known for his leadership of Tesla, SpaceX, X (formerly Twitter), and the Department of Government Efficiency (DOGE). """,
    )
    submitted = st.form_submit_button("Submit")
    if submitted:
        generate_response(text)
