
 
import streamlit as st
import requests
 
BACKEND_URL = "http://localhost:8000/ask"
 
st.title("Knowledge Hub Using AI")
st.write("Ask technical questions and get AI-generated answers from Confluence.")
 
question = st.text_area("Enter your question:")
if st.button("Ask"):
    if question:
        response = requests.post(BACKEND_URL, json={"question": question})
        if response.status_code == 200:
            st.subheader("Answer:")
            st.write(response.json().get("answer", "No response found."))
        else:
            st.error("Error fetching response.")
    else:
        st.warning("Please enter a question.")
 