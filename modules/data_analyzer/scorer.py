from normalizer import normalize_column

def apply_scores(df, market_cap_weight=0.4, eps_weight=0.3, revenue_weight=0.3):
    df['MarketCapScore'] = normalize_column(df, 'MARKET_CAP') * market_cap_weight
    df['EPSForecastScore'] = normalize_column(df, 'EPS_FORECAST') * eps_weight
    df['EPSActualScore'] = normalize_column(df, 'EPS_ACTUAL') * eps_weight
    df['RevenueForecastScore'] = normalize_column(df, 'REVENUE_FORECAST') * revenue_weight
    df['RevenueActualScore'] = normalize_column(df, 'REVENUE_ACTUAL') * revenue_weight

    df['FinalScore'] = (
        df['MarketCapScore'] +
        df['EPSForecastScore'] +
        df['EPSActualScore'] +
        df['RevenueForecastScore'] +
        df['RevenueActualScore']
    )
    return df
