import streamlit as st
from page_user_input import page_user_input
from page_display_dataset import page_display_dataset

def main():
    st.title("Marketing Analytics Dashboard")

    # Page 1: User input for dataset
    dataset = page_user_input()

    # Page 2: Display dataset, remove null values, and visualize
    page_display_dataset(dataset)

if __name__ == "__main__":
    main()
