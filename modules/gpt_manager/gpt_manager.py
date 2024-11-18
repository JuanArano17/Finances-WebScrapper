import openai
import os
import pandas as pd

class GPTManager:
    def __init__(self, api_key, output_dir_text='data/stock_texts', output_dir_csv='data/stock_tables'):
        self.api_key = api_key
        openai.api_key = api_key
        self.output_dir_text = output_dir_text
        self.output_dir_csv = output_dir_csv
        os.makedirs(self.output_dir_text, exist_ok=True)
        os.makedirs(self.output_dir_csv, exist_ok=True)

    def get_metric_data(self, stock_name, metric):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": f"You are a financial analyst providing detailed metric analysis for {stock_name}."},
                {"role": "user", "content": f"Provide the recent value (as of Q3 2024) for {metric} and interpret its impact on investment decision."}
            ]
        )
        return response['choices'][0]['message']['content'].strip()

    def gather_metrics_for_stock(self, stock_name):
        metrics = [
            "Revenue Growth Rate", "Earnings Per Share (EPS)", "Operating Margin", "Free Cash Flow (FCF)",
            "Debt-to-Equity Ratio", "Return on Equity (ROE)", "Subscriber Growth in Streaming Services",
            "Attendance and Revenue from Theme Parks", "Content Production and Acquisition Costs",
            "Market Share in Key Segments"
        ]
        stock_file_path = os.path.join(self.output_dir_text, f"{stock_name}.txt")
        
        with open(stock_file_path, 'w') as file:
            for metric in metrics:
                metric_data = self.get_metric_data(stock_name, metric)
                file.write(f"{metric}: {metric_data}\n\n")
        print(f"Metrics for {stock_name} saved to {stock_file_path}")

    def create_table_from_text(self, stock_name):
        stock_file_path = os.path.join(self.output_dir_text, f"{stock_name}.txt")
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a data analyst creating a structured table for stock analysis."},
                {"role": "user", "content": f"Create a structured table for {stock_name} with the following columns: Metric, Recent Value (as of Q3 2024), Interpretation, Impact on Investment Decision (Weight). Use the details provided in this text:\n\n{open(stock_file_path).read()}"}
            ]
        )
        table_data = response['choices'][0]['message']['content'].strip()

        # Convert table_data to pandas DataFrame (assuming the response is formatted as a list of dictionaries or in a similar structured way)
        lines = table_data.splitlines()
        data = []
        for line in lines[1:]:  # Skipping the header row
            parts = line.split("\t")
            if len(parts) == 4:
                data.append(parts)
        
        df = pd.DataFrame(data, columns=["Metric", "Recent Value (as of Q3 2024)", "Interpretation", "Impact on Investment Decision (Weight)"])
        stock_table_path = os.path.join(self.output_dir_csv, f"{stock_name}.csv")
        df.to_csv(stock_table_path, index=False)
        print(f"Table for {stock_name} saved to {stock_table_path}")

    def process_top_stocks(self, top_stocks_df):
        for stock_name in top_stocks_df['Company']:
            self.gather_metrics_for_stock(stock_name)
            self.create_table_from_text(stock_name)
