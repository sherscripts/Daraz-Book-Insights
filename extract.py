# Import necessary modules
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Make sure a 'data' directory exists to save the files
os.makedirs("data", exist_ok=True)

# Start Firefox WebDriver
driver = webdriver.Firefox()

# Initialize a counter to save files uniquely
file = 0

# Loop through the first 5 pages of the book search results
for i in range(1, 6):
    driver.get(f"https://www.daraz.com.np/catalog/?page={i}&q=books")
    driver.maximize_window()
    time.sleep(3)  # Wait for the page to load

    # Find all elements with the class name 'Ms6aG'
    elems = driver.find_elements(By.CLASS_NAME, "Ms6aG")
    print(f"Found {len(elems)} items on page {i}")

    # Loop through each item and save its HTML to a separate file
    for elem in elems:
        html_content = elem.get_attribute("outerHTML")
        with open(f"data/books_{file}.html", "w", encoding="utf-8") as f:
            f.write(html_content)
        file += 1

# Close the browser
driver.quit()
