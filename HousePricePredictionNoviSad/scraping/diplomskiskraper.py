import copy

from selenium import webdriver
from selenium.webdriver.common.by import By

import csv
import time
import json
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

PATH = 'C:/Users/aleksa/Downloads/chromedriver.exe'
OPTIONS = 'C:\Program Files\Google\Chrome\Application\chrome.exe'

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.binary_location = OPTIONS
    driver = webdriver.Chrome(ChromeDriverManager().install())
    dictionary = {}
    table_data = []
    with open('linkovi.csv', 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            # print(row)
            try:
                driver.get(row[0])
                elems = driver.find_elements(By.CLASS_NAME, "value")
                labels = driver.find_elements(By.CLASS_NAME, "label")
                address_container = driver.find_element(By.TAG_NAME, "app-place-info")
                address = address_container.find_element(By.TAG_NAME,"strong")
                location = address_container.find_element(By.TAG_NAME, "span")
                #print(lc1.text)
                time.sleep(1)
                dictionary['Adresa:'] = address.text
                dictionary['Lokacija:'] = location.text
                for i in range(len(elems)):
                    # dictionary['Lokacija'] = location.text
                    dictionary[labels[i].text] = elems[i].text
                new_dic = copy.deepcopy(dictionary)
                print(new_dic)
                table_data.append(new_dic)
            except NoSuchElementException:
                time.sleep(2)
    with open('scraped-flats.json', 'w', encoding='utf-8') as f:
        json.dump(table_data, f, sort_keys=True)
    driver.close()
