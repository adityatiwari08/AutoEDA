from dotenv import load_dotenv
import os
import streamlit as st
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI





load_dotenv()



llm = OpenAI(api_token="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")
pandas_ai =  PandasAI(llm)


st.title("PROMPT BASED DATA ANALYSIS")

uploaded_file = st.file_uploader("Upload a CSV file for analysis", type=['csv'])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head(6))
    st.write(df.tail(6))
    st.write(df.describe())
    
    prompt = st.text_area("Enter your prompt:")

    if st.button("Generate"):
        if prompt:
            st.write("Generating response...")
            st.write(pandas_ai.run(df, prompt))
        else:
            st.warning("Please enter a prompt.")
