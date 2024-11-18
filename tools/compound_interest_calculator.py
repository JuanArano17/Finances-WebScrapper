import pandas as pd
import streamlit as st
import plotly.graph_objects as go

def basic_compound_interest(principal, annual_rate, years, capitalization_periods):
    periods = years * capitalization_periods
    total_investment = principal
    investment = principal
    yearly_data = []

    for period in range(periods):
        if (period + 1) % (12 // capitalization_periods) == 0:
            interest = investment * (annual_rate / capitalization_periods)
            investment += interest

        if (period + 1) % 12 == 0:  # Log yearly data
            yearly_data.append({
                "Year": (period + 1) // 12,
                "Investment": investment,
                "Accumulated Investment": total_investment,
                "Interest Gains": investment - total_investment
            })

    yearly_data_df = pd.DataFrame(yearly_data).set_index("Year")
    relation = investment / total_investment
    return investment, total_investment, relation, yearly_data_df


def monthly_investing_compound_interest(principal, annual_rate, years, capitalization_periods, monthly_investment):
    periods = years * capitalization_periods
    investment = principal
    total_investment = principal
    accumulated_investment = 0
    yearly_data = []

    for period in range(periods):
        if (period + 1) % (12 // capitalization_periods) == 0:
            interest = investment * (annual_rate / capitalization_periods)
            investment += interest

        investment += monthly_investment
        accumulated_investment += monthly_investment
        total_investment += monthly_investment

        if (period + 1) % 12 == 0:  # Log yearly data
            yearly_data.append({
                "Year": (period + 1) // 12,
                "Investment": investment,
                "Accumulated Investment": accumulated_investment,
                "Interest Gains": investment - accumulated_investment
            })

    yearly_data_df = pd.DataFrame(yearly_data).set_index("Year")
    relation = investment / total_investment
    return investment, total_investment, relation, yearly_data_df


def incremental_monthly_investing(principal, annual_rate, years, capitalization_periods, monthly_investment, increment, increment_periods):
    periods = years * capitalization_periods
    monthly_rate = (1 + annual_rate) ** (1 / 12) - 1
    investment = principal
    total_investment = principal
    accumulated_investment = 0
    yearly_data = []

    for period in range(periods):
        if (period + 1) % increment_periods == 0:
            monthly_investment += increment

        if (period + 1) % (12 // capitalization_periods) == 0:
            interest = investment * (annual_rate / capitalization_periods)
            investment += interest

        investment += monthly_investment
        accumulated_investment += monthly_investment
        total_investment += monthly_investment

        if (period + 1) % 12 == 0:  # Log yearly data
            yearly_data.append({
                "Year": (period + 1) // 12,
                "Investment": investment,
                "Accumulated Investment": accumulated_investment,
                "Interest Gains": investment - accumulated_investment
            })

    yearly_data_df = pd.DataFrame(yearly_data).set_index("Year")
    relation = investment / total_investment
    return investment, total_investment, relation, yearly_data_df

# Utility function to abbreviate large numbers
def abbreviate_number(value):
    """Convert a number into a readable format using K, M, B abbreviations."""
    if value >= 1_000_000_000:
        return f"{value / 1_000_000_000:.1f}B"
    elif value >= 1_000_000:
        return f"{value / 1_000_000:.1f}M"
    elif value >= 1_000:
        return f"{value / 1_000:.1f}K"
    else:
        return str(value)

# Function to create an interactive Plotly chart
def plot_interactive_chart(yearly_data, title, final_amount):
    """Create an interactive Plotly chart for investment data."""
    fig = go.Figure()

    # Add Accumulated Investment trace
    fig.add_trace(go.Scatter(
        x=yearly_data.index,
        y=yearly_data['Accumulated Investment'],
        mode='lines',
        name='Accumulated Investment',
        line=dict(color='blue')
    ))

    # Add Interest Gains trace
    fig.add_trace(go.Scatter(
        x=yearly_data.index,
        y=yearly_data['Interest Gains'],
        mode='lines',
        name='Interest Gains',
        line=dict(color='orange')
    ))

    # Add final amount annotation
    fig.add_annotation(
        x=yearly_data.index[-1],
        y=final_amount,
        text=f"Final: ${final_amount:,.2f}",
        showarrow=True,
        arrowhead=1,
        ax=-40,
        ay=-40,
        font=dict(color="green", size=12, weight="bold")
    )

    # Update layout for grid lines
    fig.update_layout(
        title=title,
        xaxis=dict(
            title="Years",
            showgrid=True,  # Enable vertical grid lines
            gridcolor="lightgray",
            gridwidth=0.5
        ),
        yaxis=dict(
            title="Money",
            showgrid=True,
            gridcolor="lightgray",
            gridwidth=0.5,
            tickformat=".2s"  # Abbreviates numbers (e.g., 1M, 1K)
        ),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )

    st.plotly_chart(fig)