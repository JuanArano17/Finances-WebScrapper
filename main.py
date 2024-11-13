import pandas as pd
import re
import streamlit as st
from scraper import scrape_earnings_data  # Import the scraping function

def process_data(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()[1:]  # Skip the first line

    data = []
    pattern = re.compile(r"(.+?)\s+(\S+)\s*/\s+(\S+)\s+(\S+)\s*/\s+(\S+)\s+(\S+)")

    for line in lines:
        match = pattern.match(line.strip())
        if match:
            company = match.group(1).strip()
            eps_forecast = match.group(2) + " / " + match.group(3)
            revenue_forecast = match.group(4) + " / " + match.group(5)
            market_cap = match.group(6)

            if 'T' in market_cap:
                cap_value = float(market_cap.replace('T', '')) * 1e12
            elif 'B' in market_cap:
                cap_value = float(market_cap.replace('B', '')) * 1e9
            elif 'M' in market_cap:
                cap_value = float(market_cap.replace('M', '')) * 1e6
            elif 'K' in market_cap:
                cap_value = float(market_cap.replace('K', '')) * 1e3
            else:
                cap_value = float(market_cap)

            if cap_value >= 10e6:  # Only keep entries with cap >= 10M
                data.append({
                    "Company": company,
                    "EPS/FORECAST": eps_forecast,
                    "REVENUE/FORECAST": revenue_forecast,
                    "MARKET CAP": market_cap
                })

    df = pd.DataFrame(data)
    return df

# Streamlit App
st.title("Interactive Financial Data Table")

# Display a loading animation while scraping
with st.spinner("Scraping data, please wait..."):
    scrape_earnings_data()  # Call the scraper function to get the latest data

# Process the scraped data
input_file = 'earnings_data.txt'
df = process_data(input_file)

# Display the dataframe
st.dataframe(df, use_container_width=True)