import streamlit as st
import requests
import os

def download_pdf(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        return True
    return False

st.title("Patent Infringement Detector")

url = st.text_input("Enter the URL of your patent:")
if url:
    filename = url.split("/")[-1]
    if not filename.endswith('.pdf'):
        filename += '.pdf'
    
    save_path = os.path.join("downloads", filename)
    
    if st.button("Detect Infringement"):
        with st.spinner("Analyzing..."):
            if not os.path.exists("downloads"):
                os.makedirs("downloads")
            
            if download_pdf(url, save_path):
                st.success(f"PDF downloaded successfully and saved as {save_path}")
            else:
                st.error("Failed to download the PDF. Please check the URL and try again.")