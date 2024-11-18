import pandas as pd
from modules.data_analyzer.data_analyzer import filter_promising_stocks
from modules.gpt_manager.gpt_manager import GPTManager

# Initialize the GPTManager with your OpenAI API key
gpt_manager = GPTManager(api_key='your_openai_api_key')  # Replace with your actual API key

# Load raw data from raw_earnings_data.txt instead of using the scraper
df = pd.read_csv('txt/raw_earnings_data.txt', delimiter='\t')

# Filter the top 10 promising stocks
top_stocks_df = filter_promising_stocks(df)

# Process each top stock to gather metrics and create tables using GPT API
for stock_name in top_stocks_df['Company']:
    print(f"\nGathering metrics for {stock_name}...")
    
    # Gather each metric one at a time for better accuracy, then save each response in a .txt file
    gpt_manager.gather_metrics_for_stock(stock_name)
    
    # Create the final table for each stock using GPT-generated data
    gpt_manager.create_table_from_text(stock_name)
    
    # Print a message to indicate completion for this stock
    print(f"Completed table for {stock_name}\n")
