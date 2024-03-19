import streamlit as st
import pandas as pd

def page_user_input():
    st.title("Page 1: Dataset Input")
    st.write("Please upload the dataset (CSV format):")
    
    # File uploader for uploading dataset
    uploaded_file = st.file_uploader("Upload Dataset (CSV)", type="csv")
    
    if st.button("Next"):
        if uploaded_file is not None:
            # Read dataset into DataFrame
            try:
                dataset = pd.read_csv(uploaded_file, encoding='latin-1')
                return dataset
            except Exception as e:
                st.error(f"Error reading CSV file: {e}")
        else:
            st.error("Please upload a dataset")
