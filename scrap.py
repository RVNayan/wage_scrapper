from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


# Set up the Chrome driver
driver = webdriver.Chrome()

company = input("Please enter the company name: ")

url = f"https://www.levels.fyi/companies/{company}/salaries/software-engineer?sortOrder=ASC&offset=0&yoeChoice=junior&country=113"

driver.get(url)

text = driver.find_element(By .XPATH,'.//*[@id="blur-prompt_blurPromptCell__qv6Ha"]/div/div/button')
text.click()

text2 = driver.find_element(By .XPATH,'.//*[@id="blur-prompt_blurPromptCell__qv6Ha"]/div/div/button')
text2.click()

time.sleep(2)
bigdata = driver.find_element(By .XPATH,'.//*[@id="company-page_cardContainerId__MSgxF"]/div/div[1]/div/div[8]/table/tbody')

#taking data from a table
rows = bigdata.find_elements(By.TAG_NAME, 'tr')
for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        row_data = [cell.text for cell in cells]
        print(row_data)





















# button1 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div[7]/table/tbody/tr[5]/td/div/div/button')
# button1.click()


# time.sleep(2)
# button2 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div[7]/table/tbody/tr[5]/td/div/div/button')
# button2.click()


# time.sleep(2)

# # Find the table

# # Find all rows in the table


# # Iterate over the rows and extract the data
# def check(driver):
#     table = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div[7]/table')
#     time.sleep(5)
#     rows = table.find_elements(By.TAG_NAME, "tr")
#     for row in rows:
#         # Find all cells in the row
#         cells = row.find_elements(By.TAG_NAME, "td")

#         # Extract the text from each cell and print it
#         row_data = [cell.text for cell in cells]
#         print(row_data)

# for i in range(3):
#     check(driver)
#     button3 = driver.find_element(By.XPATH, '//button[contains(@class, "css-1f3e5dk")]')

#     button3.click()


# driver.quit()

