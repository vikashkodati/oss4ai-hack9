---
title: Patent Infringement Detector 
emoji: 📚
colorFrom: pink
colorTo: yellow
sdk: streamlit
sdk_version: 1.38.0
app_file: app.py
pinned: false
---

# Data Fetcher AI Agent

This Streamlit app identifies the extent of infringement of a corpus of papers with your patent(s) 

## Features

- Input your OpenAI API key securely
- Provide corpus of papers
- Provide your patent(s)

## How to Use

1. Enter your OpenAI API key in the sidebar (this is required to run the app)
2. Provide the set of papers

## Security Note

Your API key is not stored and is only used for the current session. It's securely handled and not displayed after entry.

## Future Improvements

- Implement real time connection to USPTO APIs
- Implement real time connection to alphaXiv 
- Constantly run agents in the background and alert the user using functions 
