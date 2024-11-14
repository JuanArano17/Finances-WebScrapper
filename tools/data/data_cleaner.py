import pandas as pd
import re

def convert_to_full_value(value):
    if not value or value == "--" or "," in value:
        return None
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
            return float(value)
        except ValueError:
            return None

def clean_data(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()[1:]

    data = []
    pattern = re.compile(r"(.+?)\s+(\S+)\s*/\s+(\S+)\s+(\S+)\s*/\s+(\S+)\s+(\S+)")

    for line in lines:
        match = pattern.match(line.strip())
        if match:
            company = match.group(1).strip()
            eps_forecast = convert_to_full_value(match.group(2))
            eps_actual = convert_to_full_value(match.group(3))
            revenue_forecast = convert_to_full_value(match.group(4))
            revenue_actual = convert_to_full_value(match.group(5))
            market_cap = convert_to_full_value(match.group(6))

            data.append({
                "Company": company,
                "EPS_FORECAST": eps_forecast,
                "EPS_ACTUAL": eps_actual,
                "REVENUE_FORECAST": revenue_forecast,
                "REVENUE_ACTUAL": revenue_actual,
                "MARKET_CAP": market_cap
            })

    return pd.DataFrame(data)
