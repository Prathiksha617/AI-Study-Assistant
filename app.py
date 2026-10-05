import streamlit as st

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="🎓"
)

st.title("🎓 AI Study Assistant")

st.write(
    "Welcome to your AI Study Assistant!"
)

st.header("📌 Sample Input")

st.code("What is Machine Learning?")

st.header("📌 Sample Output")

st.success(
    "Machine Learning is a branch of Artificial Intelligence "
    "where computers learn patterns from data and use those "
    "patterns to make predictions or decisions."
)