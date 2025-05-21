import streamlit as st
import requests
import os
import time

st.set_page_config(page_title="Infra Pilot UI", layout="wide")

st.title("🤖 Infra Pilot – Ask your Terraform")

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

# Simple question box
question = st.text_input("Ask a question about your Terraform infrastructure:", "What does this module do?")

st.markdown("---")
st.header("Generate Terraform Docs")

if st.button("Generate Markdown Documentation"):
    with st.spinner("Generating documentation..."):
        try:
            res = requests.post(f"{BACKEND_URL}/docs/generate")
            if res.ok:
                st.success("Docs generated successfully!")
                file_path = res.json().get("file", "")
                st.code(f"Saved at: {file_path}", language="markdown")
            else:
                st.error(f" Failed to generate docs: {res.text}")
        except Exception as e:
            st.error(f" Error: {str(e)}")
