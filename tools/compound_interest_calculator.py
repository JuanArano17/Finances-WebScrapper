import pandas as pd

def basic_compound_interest(principal, annual_rate, years, capitalization_periods):
    rate_per_period = annual_rate / capitalization_periods
    total_periods = years * capitalization_periods
    amount = principal * ((1 + rate_per_period) ** total_periods)
    return amount

def monthly_investing_compound_interest(principal, annual_rate, years, capitalization_periods, monthly_investment):
    total_months = years * 12
    final_amount = principal
    for month in range(total_months):
        final_amount += monthly_investment
        if (month + 1) % (12 // capitalization_periods) == 0:  # Add monthly investment at correct intervals
            final_amount *= (1 + annual_rate / capitalization_periods)
    return final_amount


def incremental_monthly_investing(principal, annual_rate, years, capitalization_periods, monthly_investment, increment, increment_periods):
    total_months = years * 12
    final_amount = principal
    current_monthly_investment = monthly_investment

    for month in range(total_months):
        final_amount += current_monthly_investment
        if (month + 1) % increment_periods == 0:  # Increment investment after each increment period
            current_monthly_investment += increment
        if (month + 1) % (12 // capitalization_periods) == 0:  # Apply interest at compounding intervals
            final_amount *= (1 + annual_rate / capitalization_periods)

    return final_amount
