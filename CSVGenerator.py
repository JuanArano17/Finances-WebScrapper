import pandas as pd
import re
import streamlit as st

def process_data(input_file):
    # Read data from input file
    with open(input_file, 'r') as file:
        lines = file.readlines()
        
    # Initialize empty list for structured data
    data = []

    for line in lines:
        # Extract the required fields using regex
        match = re.match(r"(.+?)\s+(\S+)\s+/\s+(\S+)\s+(\S+)\s+/\s+(\S+)\s+(\S+)", line.strip())
        if match:
            company = match.group(1).strip()
            eps_forecast = match.group(2) + " / " + match.group(3)
            revenue_forecast = match.group(4) + " / " + match.group(5)
            market_cap = match.group(6)

            # Convert market cap to numerical value for filtering
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

            # Filter based on market cap
            if cap_value >= 10e6:  # Only keep entries with cap >= 10M
                data.append({
                    "Company": company,
                    "EPS/FORECAST": eps_forecast,
                    "REVENUE/FORECAST": revenue_forecast,
                    "MARKET CAP": market_cap
                })

    # Convert to DataFrame
    df = pd.DataFrame(data)
    return df

# Load and process data
input_file = 'earnings_data.txt'
df = process_data(input_file)

# Set up Streamlit app
st.title("Interactive Financial Data Table")

# Display the dataframe with pagination, filtering, and sorting
st.dataframe(df, use_container_width=True)
