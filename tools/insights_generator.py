def generate_insights(df):
    insights = {
        "Average Market Cap": df['MARKET_CAP'].mean(),
        "Average EPS Forecast": df['EPS_FORECAST'].dropna().mean(),
        "Average Revenue Forecast": df['REVENUE_FORECAST'].dropna().mean()
    }
    return insights