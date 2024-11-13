from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# Initialize Safari WebDriver
driver = webdriver.Safari()

# Open the webpage
url = "https://www.investing.com/earnings-calendar/"
driver.get(url)

# Accept Cookies
try:
    accept_cookies_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
    )
    accept_cookies_button.click()
    print("Cookies accepted.")
    time.sleep(2)  # Small pause to allow any transition effect
except Exception as e:
    print("No cookies popup found or could not click the 'I Accept' button:", e)

# Click "Next Week" button
try:
    next_week_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "timeFrame_nextWeek"))
    )
    next_week_button.click()
    time.sleep(10)  # Increase wait time to allow all rows to load
except Exception as e:
    print("Could not find or click the 'Next Week' button:", e)
    driver.quit()
    exit()

# Scroll down to ensure Friday's data is fully loaded
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)  # Wait a bit for any delayed loading

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()  # Close the browser as it's no longer needed

# Locate the earnings table
table = soup.find('table', {'id': 'earningsCalendarData'})

if not table:
    print("Could not find the table with earnings data.")
    exit()

# Extract headers
headers = [header.text.strip() for header in table.find_all('th')]

# Initialize an empty list to hold row data
data_rows = []

# Loop through rows in the table
for row in table.find_all('tr'):
    columns = row.find_all('td')
    if columns:  # Ensure it's a valid data row
        row_data = [col.get_text(strip=True) for col in columns]
        data_rows.append(row_data)

# Save to a .txt file
with open("earnings_data.txt", "w") as file:
    file.write('\t'.join(headers) + '\n')
    for data_row in data_rows:
        file.write('\t'.join(data_row) + '\n')

print("Data saved to earnings_data.txt")
