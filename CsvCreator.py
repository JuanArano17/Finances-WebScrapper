import pandas as pd
import re

# Path to the .txt file containing the input data
file_path = 'input_data.txt'
# Path for the output .csv file
output_csv_path = 'output_data.csv'

# Read the content of the file
with open(file_path, 'r') as file:
    input_text = file.read()

# Eliminate extra spaces and clean up the text
cleaned_text = re.sub(r'\s+', ' ', input_text).strip()

# Define columns for the DataFrame
columns = ["Company", "EPS/FORECAST", "REVENUE/FORECAST", "MARKET CAP"]

# Initialize an empty list to store the parsed data
data = []

# Regex pattern to capture each line with the required fields
pattern = re.compile(r"(.+?) \((\w+)\) ([^\s/]+) / ([^\s]+) ([^\s/]+) / ([^\s]+) ([^\s]+)")

# Process each line in the cleaned text
for line in cleaned_text.splitlines():
    match = pattern.match(line)
    if match:
        # Extract and format the values
        company_name = f"{match.group(1)} ({match.group(2)})"
        eps_forecast = f"{match.group(3)} / {match.group(4)}"
        revenue_forecast = f"{match.group(5)} / {match.group(6)}"
        market_cap = match.group(7)

        # Append to data list
        data.append([company_name, eps_forecast, revenue_forecast, market_cap])

# Create DataFrame
df = pd.DataFrame(data, columns=columns)

# Save the DataFrame to a .csv file
df.to_csv(output_csv_path, index=False)

# Display a message to confirm that the file has been saved
print(f"Data saved to {output_csv_path}")
