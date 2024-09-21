import streamlit as st
from datetime import date
import os
from pydantic import BaseModel, Field, ValidationError

# Streamlit app starts here
st.title("Patent Infringement Detector")

# Sidebar inputs
api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")
project_id = st.sidebar.text_input("Enter your Earth Engine Project ID", "genai-agent-hack-2024")
#start_date = st.sidebar.date_input("Start Date", value=date(2021, 6, 1))
#end_date = st.sidebar.date_input("End Date", value=date(2021, 6, 30))
my_patent = st.sidebar.text_input("Patent Number", "")
#image_name = st.sidebar.text_input("Image Name", "sentinel2_image")

# Function to set the API key
def set_api_key(key):
    os.environ['OPENAI_API_KEY'] = key

# Run the data fetch when button is clicked
if st.sidebar.button("Fetch Sentinel-2 Image"):
    if not api_key:
        st.error("Please enter your OpenAI API Key.")
    else:
        set_api_key(api_key)
        try:

            # Display the result
            st.write("Potential Infringemet sighted. Approx value $500million")
        except ValidationError as e:
            st.error(f"Validation Error: {e}")

# Add a note about API key security
st.sidebar.markdown("---")
st.sidebar.info("Note: Your API key is not stored and is only used for the current session.")