# Import necessary modules
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from bs4 import BeautifulSoup
import pandas as pd
# Make sure a 'data' directory exists to save the files
os.makedirs("data", exist_ok=True)

# Start Firefox WebDriver
driver = webdriver.Firefox()
data={
    "title":[],
    "price":[],
    "link":[],
    'unit_sold':[],
    'rating_count':[],
    'stars':[]
}



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
        soup = BeautifulSoup(html_content, 'html.parser')
        title = soup.select_one("div.RfADt a").text.strip()
        link = "https:" + soup.select_one("div.RfADt a")["href"].strip()
        price = soup.select_one("span.ooOxS").text.strip()

        unit_sold_tag = soup.select_one("span._1cEkb span")
        unit_sold = unit_sold_tag.text.strip() if unit_sold_tag else "N/A"

        rating_count_tag = soup.select_one("span.qzqFw")
        rating_count = rating_count_tag.text.strip("()") if rating_count_tag else "0"
        stars = len(soup.select("i._9-ogB.Dy1nx"))




        data["title"].append(title)
        data["price"].append(price)
        data["link"].append(link)
        data["unit_sold"].append(unit_sold)
        data["rating_count"].append(rating_count)
        data["stars"].append(stars)

daraz_df=pd.DataFrame(data)
daraz_df.to_csv("raw_data.csv",index=False)
# Close the browser
driver.quit()
