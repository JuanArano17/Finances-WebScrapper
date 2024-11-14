from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

def scrape_earnings_data(output_file='earnings_data.txt'):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    url = "https://www.investing.com/earnings-calendar/"
    driver.get(url)

    # Accept Cookies and navigate
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))).click()
        time.sleep(2)
    except:
        print("No cookies popup found.")

    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "timeFrame_nextWeek"))).click()
        time.sleep(10)
    except:
        print("Could not find 'Next Week' button.")
        driver.quit()
        return

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

    # Parse HTML and save raw data
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    table = soup.find('table', {'id': 'earningsCalendarData'})

    if not table:
        print("Could not find the table with earnings data.")
        return

    with open(output_file, "w") as file:
        headers = [header.text.strip() for header in table.find_all('th')]
        file.write('\t'.join(headers) + '\n')
        for row in table.find_all('tr'):
            columns = row.find_all('td')
            if columns:
                file.write('\t'.join([col.get_text(strip=True) for col in columns]) + '\n')

    print(f"Data saved to {output_file}")