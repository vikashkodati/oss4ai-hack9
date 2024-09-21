import streamlit as st
import requests
import io
import PyPDF2

def fetch_pdf(url):
    response = requests.get(url)
    if response.status_code == 200:
        return io.BytesIO(response.content)
    return None

def analyze_pdf(pdf_content):
    # This is a placeholder function. Replace with your actual analysis logic.
    reader = PyPDF2.PdfReader(pdf_content)
    num_pages = len(reader.pages)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    
    word_count = len(text.split())
    return f"Number of pages: {num_pages}\nTotal word count: {word_count}"

st.title("Patent Infirngement Detector")

url = st.text_input("Enter the URL of the PDF file:")
if url:
    if st.button("Download and Analyze PDF for infrigement"):
        with st.spinner("Fetching and analyzing PDF..."):
            pdf_data = fetch_pdf(url)
            if pdf_data:
                # Analyze the PDF
                analysis_result = analyze_pdf(pdf_data)
                
                # Display analysis results
                st.subheader("Analysis Results:")
                st.text(analysis_result)
                
                # Offer download option
                filename = url.split("/")[-1]
                if not filename.endswith('.pdf'):
                    filename += '.pdf'
                
                st.download_button(
                    label="Download the PDF",
                    data=pdf_data,
                    file_name=filename,
                    mime="application/pdf"
                )
                st.success("PDF analyzed successfully. Partial infringement found. There are gounds to litigate.")
            else:
                st.error("Failed to fetch the PDF. Please check the URL and try again.")
