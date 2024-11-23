
# Earnings Report Scraper and Analyzer

This project is a web scraper and data analysis tool designed to collect earnings report data from [Investing.com](https://www.investing.com/earnings-calendar/) and present it in an interactive format using Streamlit. The tool gathers EPS, revenue, and market cap information for companies, allowing users to analyze potential earnings outcomes and gain financial insights.

## Purpose

The purpose of this project is to provide investors and financial analysts with streamlined access to quarterly earnings report data from publicly traded companies. By gathering and structuring important financial information in real-time, this project allows users to monitor key events, such as quarterly earnings announcements, to inform investment decisions. Understanding these events can help anticipate market reactions and gain insights into company performance and sector trends, ultimately aiding in data-driven decision-making in the stock market.

## Features

- **Web Scraping**: Automatically collects company earnings data, including EPS, revenue forecasts, and market capitalization.
- **Data Cleaning**: Cleans the scraped data by converting values with suffixes (K, M, B, T) into full float values and handling missing data appropriately.
- **Data Filtering and Sorting**: Filters data to include only companies with a significant market cap threshold (default is $1 billion) and relevant EPS or revenue data, with sorting by market cap in descending order.
- **Interactive Data Visualization**: Displays the data in a Streamlit app with two tabs:
  - **Full Data**: Shows the complete scraped and cleaned data.
  - **Filtered Data with Insights**: Presents filtered data with calculated insights, such as average market cap and average revenue forecast.
- **Loading Animation**: Provides a loading animation in the Streamlit interface while the data is being scraped.
- **Enhanced Layout**: Optimized display to utilize more screen space for better data visualization.

## Requirements

- **Python 3.7+**
- **Selenium** for web scraping
- **BeautifulSoup** for HTML parsing
- **Pandas** for data processing
- **Streamlit** for the interactive web interface

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/JuanArano17/earnings-report-scraper.git
   cd earnings-report-scraper
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   Ensure you have the necessary drivers installed for Selenium. This project is configured to use Chrome in headless mode, so make sure you have [ChromeDriver](https://sites.google.com/chromium.org/driver/) installed.

## Usage

1. **Run the Project**:
   ```bash
   streamlit run main.py
   ```

   This command will open the Streamlit app in your default web browser.

2. **How It Works**:
   - The `main.py` file initiates scraping, cleaning, filtering, and displaying the data through Streamlit.
   - On startup, the app shows a loading animation while the scraper gathers data.
   - The data is cleaned, filtered by market cap and relevance, and then displayed in an interactive table.

## Project Structure

```plaintext
├── txt/
│   ├── raw_earnings_data.txt       # Raw data file after scraping
├── csv/
│   ├── filtered_earnings_data.csv   # CSV file of the cleaned and filtered data
├── main.py                          # Main script for running the Streamlit app
├── tools/
│   ├── scrapers/
│   │   └── scraper.py               # Web scraping logic
│   ├── data/
│   │   ├── data_cleaner.py          # Data cleaning and processing
│   │   ├── data_analyzer.py         # Filtering and insights generation
│   │   └── data_saver.py            # Saving filtered data to CSV
├── static/
│   └── style.css                    # Custom CSS for Streamlit UI enhancements
├── requirements.txt                 # List of Python packages required
└── README.md                        # Project documentation
```

## Configuration

- Modify the target URL or adjust the CSS selectors in `scraper.py` if there are changes in the structure of [Investing.com](https://www.investing.com/earnings-calendar/).
- Customize the `market_cap_threshold` parameter in `data_analyzer.py` to set different filtering criteria based on market cap.
- Adjust CSS styling in `style.css` to further customize the appearance of the Streamlit app.

## Example Data

Sample data collected:

| ID | Company                  | EPS_FORECAST | EPS_ACTUAL | REVENUE_FORECAST | REVENUE_ACTUAL | MARKET_CAP   |
|----|---------------------------|--------------|------------|-------------------|----------------|--------------|
| 1  | NVIDIA (NVDA)            | None         | 0.7435     | None             | 32,970,000,000 | 3,580,000,000,000 |
| 2  | Walmart (WMT)            | None         | 0.53       | None             | 167,610,000,000| 688,240,000,000 |
| 3  | American Eagle (AEO)     | None         | 0.47       | None             | 1,310,000,000  | 3,510,000,000 |
| ...| ...                       | ...          | ...        | ...              | ...            | ...          |

## Known Issues

- If the webpage structure changes, the CSS selectors in `scraper.py` may need to be updated.
- ChromeDriver must be properly configured for Selenium, and it may require updates depending on Chrome browser versions.

## Future Enhancements

- Add sentiment analysis based on analyst recommendations or earnings call transcripts.
- Expand data filtering and sorting options within the Streamlit app.
- Integrate additional economic indicators for deeper insights.
- Add further customization in the Streamlit UI to allow user-driven parameter adjustments.

## License

This project is licensed under the MIT License.

## Author

Created by Juan Arano.
