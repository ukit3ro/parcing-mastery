import time
from selenium import webdriver
import random
from selenium.webdriver.common.by import By

agends = ['alwx', 'gene', 'bro']

url = 'https://vk.com'
options = webdriver.ChromeOptions()
#options.add_argument(f'user-agent={random.choice(agends)}')
#options.add_argument('--proxy-server=138.128.91.65:8000')
driver = webdriver.Chrome(options=options)

try:
    driver.get(url=url)
    time.sleep(5)
    email_input = driver.find_element(By.NAME, 'login')
    email_input.clear()
    email_input.send_keys('+79681106397')
    
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

