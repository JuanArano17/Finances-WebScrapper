# main.py
import pandas as pd
import re
import streamlit as st
from scraper import scrape_earnings_data  # Import the scraping function
from data_cleaner import process_data  # Import the data processing function
from tools.data_saver import save_to_csv  # Import the CSV saving function

# Streamlit App
st.title("Interactive Financial Data Table")

# Display a loading animation while scraping
with st.spinner("Scraping data, please wait..."):
    scrape_earnings_data('earnings_data.txt')  # Call the scraper function to get the latest data

# Process the scraped data
df = process_data('earnings_data.txt')

# Save processed data to CSV
save_to_csv(df, 'processed_earnings_data.csv')  # Saves the DataFrame to a CSV file

# Display the DataFrame in Streamlit
st.dataframe(df, use_container_width=True)