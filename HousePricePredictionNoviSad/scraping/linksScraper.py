from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import pandas as pd
import csv
import time
import copy
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

PATH = 'C:/Users/aleksa/Downloads/chromedriver.exe'
OPTIONS = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
ITERATE_FINISH = 100
ITERATE_START = 1

if __name__ == '__main__':
    s = Service(PATH)
    options = webdriver.ChromeOptions()
    options.binary_location = OPTIONS
    driver = webdriver.Chrome(ChromeDriverManager().install())
    for page in range(ITERATE_START, ITERATE_FINISH):
        url = 'https://www.4zida.rs/prodaja-stanova/novi-sad'
        page_num = '?strana=' + str(page)
        driver.get(url + page_num)
        # try:
        #     main = WebDriverWait(driver,10).until(
        #         EC.presence_of_element_located((By.CLASS_NAME, "app-body"))
        #     )
        #     print(main.text)
        links = driver.find_elements(By.TAG_NAME, "app-ad-search-preview-compact")
        hrefs = []
        for link in links:
            pick = link.find_element(By.TAG_NAME, "app-link")
            # print(pick.text)
            elem = pick.find_element(By.TAG_NAME, "a")
            href = elem.get_attribute('href')
            print(href)
            hrefs.append(href)
        time.sleep(1.5)
        with open('../diplomski/scraping/linkovi.csv', 'w', encoding='utf-8') as f:
            writer = csv.writer(f)
            for hr in hrefs:
                writer.writerow([hr])
    driver.close()

