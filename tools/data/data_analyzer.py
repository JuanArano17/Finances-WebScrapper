import pandas as pd

def filter_relevant_stocks(df, market_cap_threshold=1e9):
    relevant_stocks = df[df['MARKET_CAP'] >= market_cap_threshold]
    relevant_stocks = relevant_stocks[
        pd.notnull(relevant_stocks['EPS_FORECAST']) |
        pd.notnull(relevant_stocks['EPS_ACTUAL']) |
        pd.notnull(relevant_stocks['REVENUE_FORECAST']) |
        pd.notnull(relevant_stocks['REVENUE_ACTUAL'])
    ].reset_index(drop=True)
    relevant_stocks = relevant_stocks.sort_values(by='MARKET_CAP', ascending=False).reset_index(drop=True)
    return relevant_stocks