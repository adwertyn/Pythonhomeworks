import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get('https://demoblaze.com')
laptop_chapter = driver.find_element(By.LINK_TEXT, 'Laptops')
laptop_chapter.click()
next = driver.find_element(By.ID, "next2")
next.click()

time.sleep(3)
all_laptops = []
items = driver.find_elements(By.CLASS_NAME, 'row')

for item in items:
    name = item.find_element(By.TAG_NAME, 'h4').text
    price = item.find_element(By.TAG_NAME, 'h5').text
    description = item.find_element(By.TAG_NAME, 'p').text
    all_laptops.append({
                'name': name,
                'price': price,
                'description': description
            })
with open('laptops.json', 'w', encoding='utf-8') as file:
    json.dump(all_laptops, file, indent=4)
time.sleep(5)
driver.quit()
