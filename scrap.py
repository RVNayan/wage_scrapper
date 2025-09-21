from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

def main():
    company = input("Enter company slug (e.g., google): ").strip()
    user_country = input("Enter country (e.g., United States): ").strip()

    url = f"https://www.levels.fyi/companies/{company}/salaries/software-engineer?sortOrder=ASC&offset=0&yoeChoice=junior&country=113"

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get(url)

    # -----------------------------
    # Step 1: Click country selection
    # -----------------------------
    try:
        country_button = wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, "job-family_locationSelectionButton__qVpd2")
        ))
        country_button.click()
        print("Clicked country dropdown!")
    except Exception as e:
        print("Country selection button not found:", e)
        driver.quit()
        return

    # -----------------------------
    # Step 2: Get list of available countries
    # -----------------------------
    time.sleep(1)
    try:
        country_list_container = driver.find_element(By.CLASS_NAME, "css-q1c362")
        country_elements = country_list_container.find_elements(By.TAG_NAME, "li")
        countries_available = [c.text.strip() for c in country_elements]
        print("Available countries:", countries_available)
    except Exception as e:
        print("Could not read country list:", e)
        driver.quit()
        return

    # -----------------------------
    # Step 3: Validate user country
    # -----------------------------
    if user_country not in countries_available:
        print(f"Country '{user_country}' not in list. Please enter a valid country.")
        driver.quit()
        return
    else:
        # Click the country in the list
        for c in country_elements:
            if c.text.strip() == user_country:
                c.click()
                print(f"Selected country: {user_country}")
                break

    # -----------------------------
    # Step 4: Click expand button to reveal table
    # -----------------------------
    time.sleep(1)
    try:
        expand_button = wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, "css-y5b368")  # may need adjustment if class changes
        ))
        expand_button.click()
        print("Clicked expand button!")
    except Exception as e:
        print("Expand button not found or already expanded:", e)

    # -----------------------------
    # Step 5: Scrape table
    # -----------------------------
    time.sleep(2)  # wait for table to fully load
    soup = BeautifulSoup(driver.page_source, "lxml")
    table = soup.find("table")
    if table:
        for row in table.find_all("tr"):
            cells = [c.get_text(strip=True) for c in row.find_all(["td", "th"])]
            print(cells)
    else:
        print("No table found!")

    driver.quit()


if __name__ == "__main__":
    main()
