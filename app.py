import streamlit as st

st.title("🤖 AI Study Assistant")

st.write("Ask a question and get help with your studies.")

question = st.text_area("Enter your question:")

if st.button("Get Answer"):
    if question:
        st.success("Your question was received!")
        st.write("AI Answer:")
        st.write(
            "This is a simple AI Study Assistant. "
            "An AI model can be connected here to generate an answer."
        )
    else:
        st.warning("Please enter a question.")
