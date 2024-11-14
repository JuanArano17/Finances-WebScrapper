import streamlit as st
from tools.scrapers.scraper import scrape_earnings_data
from tools.data.data_cleaner import clean_data
from tools.data.data_analyzer import filter_relevant_stocks, generate_insights
from tools.data.data_saver import save_to_csv


st.set_page_config(layout="wide")
st.title("Interactive Financial Data Table and Insights")

with st.spinner("Scraping data, please wait a few seconds...(12 aprox)"):
    scrape_earnings_data('txt/raw_earnings_data.txt')
df = clean_data('txt/raw_earnings_data.txt')

relevant_df = filter_relevant_stocks(df)
insights = generate_insights(relevant_df)

save_to_csv(relevant_df, 'csv/filtered_earnings_data.csv')

tab1, tab2 = st.tabs(["Full Data", "Filtered Data with Insights"])

with tab1:
    st.subheader("Full Financial Data Table")
    st.dataframe(df, use_container_width=True)  # Ensures the dataframe uses maximum container width

with tab2:
    st.subheader("Filtered Financial Data Table")
    st.dataframe(relevant_df, use_container_width=True)  # Ensures the dataframe uses maximum container width
    st.write("""
    **Reasons for Filtering:**
    - Stocks with a market cap below the threshold of 1 billion are excluded.
    - Stocks with no meaningful EPS or revenue data (both forecast and actual missing) are excluded.
    """)
    st.subheader("Insights")
    for key, value in insights.items():
        st.write(f"{key}: {value}")
