import streamlit as st
from tools.scraper import scrape_earnings_data
from tools.data.data_cleaner import clean_data
from tools.data.data_analyzer import filter_relevant_stocks
from tools.data.data_saver import save_to_csv
from tools.insights_generator import generate_insights
from tools.compound_interest_calculator import (
    basic_compound_interest,
    find_breakeven_point_incremental,
    monthly_investing_compound_interest,
    incremental_monthly_investing,
    plot_interactive_chart,
    plot_monthly_investments_and_gains 
)

# Streamlit configuration
st.set_page_config(layout="wide")
st.title("Interactive Financial Data, Insights, and Tools")

# Tabs for different functionalities
tab1, tab2 = st.tabs(["Data Analysis", "Compound Interest Calculator"])

# Tab 1: Data Analysis
with tab1:
    st.subheader("Data Analysis")

    if st.button("Fetch Data (Scraper)"):
        with st.spinner("Scraping data, please wait..."):
            scrape_earnings_data('data/raw_earnings_data.txt')
            st.success("Data fetched successfully!")

    try:
        clean_data_df = clean_data('data/raw_earnings_data.txt')
        relevant_df = filter_relevant_stocks(clean_data_df)
        insights = generate_insights(relevant_df)
        save_to_csv(relevant_df, 'data/filtered_earnings_data.csv')

        subtab1, subtab2 = st.tabs(
            ["Full Data", "Filtered Data with Insights"])

        with subtab1:
            st.subheader("Full Financial Data Table")
            st.dataframe(clean_data_df, use_container_width=True)

        with subtab2:
            st.subheader("Filtered Financial Data Table")
            st.dataframe(relevant_df, use_container_width=True)
            st.write("""
            **Reasons for Filtering:**
            - Stocks with a market cap below the threshold of 1 billion are excluded.
            - Stocks with no meaningful EPS or revenue data (both forecast and actual missing) are excluded.
            """)
            st.subheader("Insights")
            for key, value in insights.items():
                st.write(f"{key}: {value}")
    except FileNotFoundError:
        st.warning(
            "No data found. Please fetch the data using the scraper button.")

# Tab 2: Compound Interest Calculator
with tab2:
    st.subheader("Compound Interest Calculator")

    mode = st.selectbox(
        "Select Mode", ["Basic", "Monthly Investing", "Incremental Monthly Investing"])

    principal = st.number_input(
        "Initial Investment", min_value=0.0, step=100.0)
    annual_rate = st.number_input(
        "Annual Interest Rate (%)", min_value=0.0, step=0.1) / 100
    years = st.number_input("Number of Years", min_value=1, step=1)
    capitalization_period = st.selectbox("Capitalization Frequency", [
                                         "Monthly", "Quarterly", "Semi-Annual", "Annual"])
    capitalization_map = {"Monthly": 12,
                          "Quarterly": 4, "Semi-Annual": 2, "Annual": 1}
    capitalization_periods = capitalization_map[capitalization_period]

    if mode == "Basic":
        if st.button("Calculate (Basic)"):
            final_amount, total_investment, relation, yearly_data = basic_compound_interest(
                principal, annual_rate, years, capitalization_periods
            )
            st.write(f"Final Amount: ${final_amount:,.2f}")
            st.write(f"Relation (Final Amount / Total Investment): {relation:.2f}")

            plot_interactive_chart(yearly_data, "Basic Compound Interest Over Time", final_amount)

    elif mode == "Monthly Investing":
        monthly_investment = st.number_input("Monthly Investment Amount", min_value=0.0, step=10.0)
        if st.button("Calculate (Monthly Investing)"):
            final_amount, total_investment, relation, yearly_data = monthly_investing_compound_interest(
                principal, annual_rate, years, capitalization_periods, monthly_investment
            )
            st.write(f"Final Amount: ${final_amount:,.2f}")
            st.write(f"Total Investment (excluding initial): ${total_investment:,.2f}")
            st.write(f"Relation (Final Amount / Total Investment): {relation:.2f}")

            plot_interactive_chart(yearly_data, "Monthly Investing Compound Interest Over Time", final_amount)

    elif mode == "Incremental Monthly Investing":
        monthly_investment = st.number_input("Monthly Investment Amount", min_value=0.0, step=10.0)
        increment = st.number_input("Incremental Amount", min_value=0.0, step=10.0)
        increment_periods = st.number_input("Increment Period (Months)", min_value=1, step=1)
        
        if st.button("Calculate (Incremental)"):
            final_amount, total_investment, relation, yearly_data = incremental_monthly_investing(
                principal, annual_rate, years, capitalization_periods, monthly_investment, increment, increment_periods
            )
            breakeven_month, breakeven_year = find_breakeven_point_incremental(
                principal, annual_rate, years, capitalization_periods, monthly_investment, increment, increment_periods
            )
            st.write(f"Final Amount: ${final_amount:,.2f}")
            st.write(f"Total Investment (excluding initial): ${total_investment:,.2f}")
            st.write(f"Relation (Final Amount / Total Investment): {relation:.2f}")
            if breakeven_month:
                st.write(f"Breakeven Point: {breakeven_month} months (Year {breakeven_year})")
            else:
                st.write("No breakeven point reached within the selected timeframe.")
            
            # Plot the results
            plot_interactive_chart(yearly_data, "Incremental Monthly Investing Compound Interest Over Time", final_amount)
            plot_monthly_investments_and_gains(
                principal, 
                annual_rate, 
                years, 
                monthly_investment, 
                increment, 
                increment_periods
            )
