import requests
from bs4 import BeautifulSoup
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "https://svoefermerstvo.ru/catalog/traktory"
headers = {
    "Accept": "/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 "
                  "Safari/537.36 "
}


def get_pages_list(url):
    pages = []
    driver = webdriver.Chrome()
    driver.get(url)
    page1 = driver.find_element(By.TAG_NAME, 'html')
    for q in range(265):
        page1.send_keys(Keys.DOWN)
    for j in range(2, 55):
        if j <= 4:
            button = driver.find_element(By.XPATH, f'//*[@id="viewport"]/main/div/div[3]/div[2]/div/div[3]/div/div[3]/nav/div/button[7]')    
        else:
            button = driver.find_element(By.XPATH, f'//*[@id="viewport"]/main/div/div[3]/div[2]/div/div[3]/div/div[3]/nav/div/button[8]')
        pages.append(driver.current_url)
        print(driver.current_url)
        button.click()
        time.sleep(4)
        page = driver.find_element(By.TAG_NAME, 'html')
        for s in range(293):
            page.send_keys(Keys.DOWN)
        
    with open('pages_list.txt', 'a') as file:
        for line in pages:
            file.write(f'{line}\n')

'//*[@id="viewport"]/main/div/div[3]/div[2]/div/div[3]/div/div[3]/nav/div/button[7]'
'//*[@id="viewport"]/main/div/div[3]/div[2]/div/div[3]/div/div[3]/nav/div/button[8]'
'//*[@id="viewport"]/main/div/div[3]/div[2]/div/div[3]/div/div[3]/nav/div/button[7]'
'//*[@id="viewport"]/main/div/div[3]/div[2]/div/div[3]/div/div[3]/nav/div/button[8]'
'//*[@id="viewport"]/main/div/div[3]/div[2]/div/div[3]/div/div[3]/nav/div/button[8]'
'//*[@id="viewport"]/main/div/div[3]/div[2]/div/div[3]/div/div[3]/nav/div/button[8]'


def main():
    get_pages_list(url=link)

if __name__ == "__main__":
    main()