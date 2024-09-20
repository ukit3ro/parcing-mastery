from bs4 import BeautifulSoup
import json
import os
import requests
import os
import time
import random

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
}


def get_table_page(url):
    r = requests.get(url, headers=headers)
    
    with open('index.html', 'w', encoding='utf-8') as file:
        file.write(r.text)
    
    
    
def form_position():
    with open('index.html', encoding='utf-8') as file:
        src = file.read()    
    soup = BeautifulSoup(src, 'lxml')
    table = soup.find('div', class_='table-responsive table').find('tbody').find_all('tr')
    table_name = soup.find_all('h3')[2].text
    mest = soup.find_all('h3')[3].text.strip()
    count = 0
    pts = []
    for i in table:
        tds = i.find_all('td')
        id = tds[1].text
        priority = int(tds[2].text)
        original = tds[6].text
        if tds[3].text != '':
            points = int(tds[3].text)
        else: points = 0
        """ print(points) """
        if points > 229 and original == 'Да' and priority <= 2:
            count += 1
    print(len(original))
    print(f'{table_name}, позиция: {count}, {mest}')



list = ['https://priem.guap.ru/bach/lists/list_1_515_1_1_1_f_1', 'https://priem.guap.ru/bach/lists/list_1_510_1_1_1_f_1', 'https://priem.guap.ru/bach/lists/list_1_32_1_1_1_f_1', 'https://priem.guap.ru/bach/lists/list_1_26_1_1_2_f_1', 'https://priem.guap.ru/bach/lists/list_1_70_1_1_1_f_1']




def main():
    for i in list:
        get_table_page(i)
        form_position()

if __name__ == '__main__':
    main()