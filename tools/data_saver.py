import pandas as pd

def save_to_csv(df, filename='earnings_data.csv'):
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")