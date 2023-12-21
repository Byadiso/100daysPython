
from bs4 import BeautifulSoup
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By

import time

header = {
    "user-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Mobile Safari/537.36",
    "Accept-Language": "en-GB; en-US; q=0.9;en;q=0.8"
}

url_rent = "https://appbrewery.github.io/Zillow-Clone/"

page = requests.get(url_rent, headers=header)
soup = BeautifulSoup(page.content, 'html.parser')

elements_rents = soup.find_all("div", class_="StyledPropertyCardDataWrapper")


links_addresses = []
price_list = []

address_list = []

for job_element in elements_rents:
    description = job_element.find("address", attrs={'data-test': True})
    price = job_element.find("span", class_="PropertyCardWrapper__StyledPriceLine")
    location_link = job_element.find("a", class_="StyledPropertyCardDataArea-anchor")

    location_link = location_link.get('href')
    price = price.text.split('/')[0].replace('+','')
    address = description.text.strip()

    price_list.append(price)
    links_addresses.append(location_link)
    address_list.append(address)

print(links_addresses)
print(price_list)
print(address_list)

# selenium logic
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)


for n in range(len(links_addresses)):

    url_form = "https://docs.google.com/forms/d/e/1FAIpQLSerFDXCiKNPDLFHTFl6vnkQEoWS3Khh_W6fMWyRsE0GhDn3fQ/viewform?usp=sf_link"
    driver.get(url_form)
    time.sleep(2)

    address_field = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_field = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_field = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    submit_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    address_field.send_keys(address_list[n])
    price_field.send_keys(price_list[n])
    link_field.send_keys(links_addresses[n])
    submit_button.click()

driver.quit()

