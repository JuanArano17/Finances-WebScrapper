# Earnings Report Scraper and Analyzer

This project is a web scraper and data analysis tool designed to collect earnings report data from [Investing.com](https://www.investing.com/earnings-calendar/) and present it in an interactive format using Streamlit. The tool gathers EPS, revenue, and market cap information for companies, allowing users to analyze potential earnings outcomes and gain financial insights.

## Purpose

The purpose of this project is to provide investors and financial analysts with streamlined access to quarterly earnings report data from publicly traded companies. By gathering and structuring important financial information in real-time, this project allows users to monitor key events, such as quarterly earnings announcements, to inform investment decisions. Understanding these events can help anticipate market reactions and gain insights into company performance and sector trends, ultimately aiding in data-driven decision-making in the stock market.

## Features

- **Web Scraping**: Automatically collects company earnings data, including EPS, revenue forecasts, and market capitalization.
- **Data Filtering and Sorting**: Filters data to include only companies with a market cap of $10 million or higher.
- **Interactive Data Visualization**: Displays the data in a Streamlit app, allowing users to filter, sort, and analyze earnings information in an easy-to-use interface.
- **Loading Animation**: Indicates the progress of data scraping to enhance user experience.

## Requirements

- **Python 3.7+**
- **Selenium** for web scraping
- **BeautifulSoup** for HTML parsing
- **Pandas** for data processing
- **Streamlit** for the interactive web interface

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/earnings-report-scraper.git
   cd earnings-report-scraper
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   Ensure you have the necessary drivers installed for Selenium. This project is configured to use Safari, so make sure you have [Safari WebDriver](https://developer.apple.com/documentation/webkit/testing_with_webdriver_in_safari) installed.

## Usage

1. **Run the Project**:
   ```bash
   streamlit run main.py
   ```

   This command will open the Streamlit app in your default web browser.

2. **How It Works**:
   - The `main.py` file handles both the scraping and the Streamlit interface.
   - When the application starts, it will display a loading animation while the scraper gathers data.
   - Once the data is collected, it will be displayed as an interactive table in the Streamlit app.

## Project Structure

```plaintext
├── earnings_data.txt            # Generated file with scraped earnings data
├── main.py                       # Main script to run the scraper and Streamlit app
├── InputScrapper.py              # Web scraping script for gathering earnings data
├── requirements.txt              # List of Python packages required
└── README.md                     # Project documentation
```

## Configuration

- Modify the target URL or adjust the CSS selectors in `srapper.py` if there are changes in the structure of [Investing.com](https://www.investing.com/earnings-calendar/).
- The minimum market cap filter (10M) can be adjusted in the `process_data` function in `main.py`.

## Example Data

Sample data collected:
| Company            | EPS/FORECAST | REVENUE/FORECAST | MARKET CAP |
|--------------------|--------------|-------------------|------------|
| NVIDIA (NVDA)      | 0.7435       | 32.97B           | 3.58T      |
| Walmart (WMT)      | 0.53         | 167.61B          | 688.24B    |
| American Eagle (AEO) | 0.47       | 1.31B            | 3.51B      |

## Known Issues

- If the webpage structure changes, the CSS selectors in `scrapper.py` may need to be updated.
- Safari WebDriver must be properly configured, and pop-ups must be enabled in Safari Preferences.

## Future Enhancements

- Add sentiment analysis based on analyst recommendations or earnings call transcripts.
- Expand data filtering and sorting options within the Streamlit app.
- Integrate additional economic indicators for deeper insights.

## License

This project is licensed under the MIT License.

## Author

Created by Juan Arano.
