import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chromedriver_path = "/usr/local/bin/chromedriver"

driver = webdriver.Chrome()

company = input("Please enter the company name: ")

url = f"https://www.levels.fyi/companies/{company}/salaries/software-engineer?yoeChoice=junior&country=113"

driver.get(url)

# Click the first button
button1 = driver.find_element(By.XPATH, '//*[@id="blur-prompt_blurPromptCell__qv6Ha"]/div/div/button')
button1.click()

# Wait for the second button to appear
time.sleep(2)

# Click the second button
button2 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div[8]/table/tbody/tr[5]/td/div/div/button')
button2.click()

# Wait for the table to load
time.sleep(4)

# Find the table
def check(driver):
    table = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[1]/div/div[8]/table/tbody')

# Find all rows in the table
    rows = table.find_elements(By.TAG_NAME, "tr")

# Iterate over the rows and extract the data
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")

        row_data = [cell.text for cell in cells]
        print(row_data)

for i in range(10):
    check(driver)
    button3 = driver.find_element(By.CSS_SELECTOR, ".MuiButton-root.MuiButton-text.MuiButton-textPrimary.MuiButton-sizeSmall.MuiButton-textSizeSmall.MuiButtonBase-root.css-1f3e5dk")
    button3.click() 
    time.sleep(5)
# Clean up and close the browser
driver.quit()

