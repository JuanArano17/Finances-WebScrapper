import pandas as pd
import re

def convert_to_full_value(value):
    """Convert values with K, M, B, T suffixes to full floats, or return -1.0 for missing or invalid data."""
    if not value or value == "--" or "," in value:  # Check for missing data and commas
        return -1.0  # Return -1.0 for missing or invalid data
    elif "T" in value:
        return float(value.replace("T", "")) * 1e12
    elif "B" in value:
        return float(value.replace("B", "")) * 1e9
    elif "M" in value:
        return float(value.replace("M", "")) * 1e6
    elif "K" in value:
        return float(value.replace("K", "")) * 1e3
    else:
        try:
            return float(value)  # Return as float if no suffix is present
        except ValueError:
            return -1.0  # In case of unexpected format, return -1.0


def process_data(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()[1:]  # Skip the first line

    data = []
    pattern = re.compile(r"(.+?)\s+(\S+)\s*/\s+(\S+)\s+(\S+)\s*/\s+(\S+)\s+(\S+)")

    for line in lines:
        match = pattern.match(line.strip())
        if match:
            company = match.group(1).strip()
            
            # Convert EPS and revenue forecast fields
            eps_forecast = f"{convert_to_full_value(match.group(2))} / {convert_to_full_value(match.group(3))}"
            revenue_forecast = f"{convert_to_full_value(match.group(4))} / {convert_to_full_value(match.group(5))}"
            
            # Convert market cap field
            market_cap = convert_to_full_value(match.group(6))

            # Filter out entries with a market cap below 10 million
            if market_cap >= 10e6:
                data.append({
                    "Company": company,
                    "EPS/FORECAST": eps_forecast,
                    "REVENUE/FORECAST": revenue_forecast,
                    "MARKET CAP": market_cap
                })

    df = pd.DataFrame(data)
    return df