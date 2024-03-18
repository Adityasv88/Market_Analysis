import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def page_display_dataset(dataset):
    st.title("Page 2: Displaying Dataset")
    
    if dataset is not None:
        # Ignore first three columns (customer IDs)
        dataset = dataset.iloc[:, 3:]
        
        # Display raw dataset
        st.subheader("Raw Dataset:")
        st.write(dataset.head())
        
        # Remove null values
        dataset_cleaned = dataset.dropna()
        
        # Display cleaned dataset
        st.subheader("Cleaned Dataset (Removed Null Values):")
        st.write(dataset_cleaned.head())
        
        # Visualize dataset
        st.subheader("Visualization of Dataset:")
        visualize_dataset(dataset_cleaned)

def visualize_dataset(dataset):
    # Example: Plot different graphs for dataset visualization
    numeric_columns = dataset.select_dtypes(include="number").columns
    categorical_columns = dataset.select_dtypes(exclude="number").columns
    
    # Histogram for numeric columns
    for column in numeric_columns:
        st.write(f" {column}:")
        plt.figure(figsize=(8, 6))
        sns.histplot(dataset[column], bins=20, kde=True)
        plt.xlabel(column)
        plt.ylabel("Frequency")
        st.pyplot()
    
    # Count plot for categorical columns
    for column in categorical_columns:
        st.write(f"Count Plot of {column}:")
        plt.figure(figsize=(8, 6))
        sns.countplot(data=dataset, x=column)
        plt.xlabel(column)
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        st.pyplot()
