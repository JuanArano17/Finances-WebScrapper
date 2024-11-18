import pandas as pd
from scorer import apply_scores

def filter_promising_stocks(df, market_cap_weight=0.4, eps_weight=0.3, revenue_weight=0.3, top_n=10):
    df = df.fillna(0)
    df = apply_scores(df, market_cap_weight, eps_weight, revenue_weight)
    top_stocks = df.sort_values(by='FinalScore', ascending=False).head(top_n).reset_index(drop=True)
    columns_to_keep = ['Company', 'MARKET_CAP', 'EPS_FORECAST', 'EPS_ACTUAL', 'REVENUE_FORECAST', 'REVENUE_ACTUAL', 'FinalScore']
    return top_stocks[columns_to_keep]