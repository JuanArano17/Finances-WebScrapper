import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import matplotlib.pyplot as plt

def plot_total_index_holdings(yearly_data, title):
    """
    Plots the total index holding, combining accumulated investment and interest gains.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(
        yearly_data.index, 
        yearly_data['Investment'], 
        label='Total Index Holding (Accumulated + Gains)'
    )
    plt.title(title)
    plt.xlabel("Years")
    plt.ylabel("Total Value ($)")
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)  # Integrate with Streamlit

def plot_monthly_investments_and_gains(principal, annual_rate, years, monthly_investment, increment, increment_periods):
    """
    Plots the monthly investment amounts and monthly index gains over time.
    """
    total_months = years * 12
    monthly_rate = (1 + annual_rate) ** (1 / 12) - 1  # Monthly interest rate
    current_investment = monthly_investment
    investment = principal
    monthly_data = []

    # Generate data for investments and gains
    for month in range(1, total_months + 1):
        # Calculate monthly index gain
        monthly_gain = investment * monthly_rate

        # Log data for the current month
        monthly_data.append({
            "Month": month,
            "Monthly Investment": current_investment,
            "Monthly Index Gain": monthly_gain
        })

        # Update investment
        investment += current_investment + monthly_gain

        # Increment the monthly investment periodically
        if month % increment_periods == 0:
            current_investment += increment

    # Convert to DataFrame for easy visualization
    monthly_df = pd.DataFrame(monthly_data)

    # Add Year labels with months for better x-axis representation
    monthly_df["Year (Months)"] = [
        f"{month // 12 + 1} ({month} m)" for month in monthly_df["Month"]
    ]

    # Plot both monthly investments and gains
    plt.figure(figsize=(12, 6))
    plt.bar(
        monthly_df["Month"], 
        monthly_df["Monthly Investment"], 
        color="blue", 
        label="Monthly Investment"
    )
    plt.plot(
        monthly_df["Month"], 
        monthly_df["Monthly Index Gain"], 
        color="orange", 
        label="Monthly Index Gain",
        linewidth=2
    )

    # Set x-axis labels
    plt.xticks(
        ticks=monthly_df["Month"][monthly_df["Month"] % 12 == 0],  # Yearly intervals
        labels=monthly_df["Year (Months)"][monthly_df["Month"] % 12 == 0], 
        rotation=45, 
        ha='right'
    )
    plt.title("Monthly Investments and Index Gains Over Time")
    plt.xlabel("Years (Months)")
    plt.ylabel("Amount ($)")
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Display the plot
    st.pyplot(plt)

    # Display the table in Streamlit
    st.subheader("Monthly Investments and Index Gains Table")
    st.dataframe(monthly_df[["Year (Months)", "Monthly Investment", "Monthly Index Gain"]].style.format({
        "Monthly Investment": "${:,.2f}",
        "Monthly Index Gain": "${:,.2f}"
    }), use_container_width=True)

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

    # Add Total Index Holdings (Investment) trace
    fig.add_trace(go.Scatter(
        x=yearly_data.index,
        y=yearly_data['Investment'],
        mode='lines',
        name='Total Index Holdings',
        line=dict(color='green')
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

def find_breakeven_point_incremental(principal, annual_rate, years, capitalization_periods, monthly_investment, increment, increment_periods):
    """
    Finds the breakeven point where the monthly index gain equals the monthly investment,
    accounting for incremental monthly investments.
    """
    periods = years * 12
    monthly_rate = (1 + annual_rate) ** (1 / 12) - 1
    investment = principal
    breakeven_month = None
    current_monthly_investment = monthly_investment

    for month in range(1, periods + 1):
        # Calculate the monthly gain
        monthly_gain = investment * monthly_rate

        # Check for breakeven
        if monthly_gain >= current_monthly_investment and breakeven_month is None:
            breakeven_month = month
            break

        # Increment the monthly investment periodically
        if month % increment_periods == 0:
            current_monthly_investment += increment

        # Update investment value
        investment += current_monthly_investment
        investment += investment * (annual_rate / capitalization_periods)

    if breakeven_month:
        breakeven_year = breakeven_month // 12
        return breakeven_month, breakeven_year + 1 if breakeven_month % 12 == 0 else breakeven_year
    else:
        return None, None  # No breakeven point within the given time frame