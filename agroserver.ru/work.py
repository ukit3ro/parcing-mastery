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

def get_data_file():
    if not os.path.exists('data'):
        os.mkdir('data')
    
    base = 'https://agroserver.ru/zapchasti/Y2l0eT18cmVnaW9uPXxjb3VudHJ5PXxtZXRrYT18c29ydD0xfGFjY2VwdF9nZT0x/'
    for i in range(1, 23):
        req = requests.get(f'{base}{i}/', headers=headers)
        with open(f'data/page_{i}.html', 'w', encoding='utf-8') as file:
            file.write(req.text)
        time.sleep(random.randint(20, 40))


def collect_data():
    data_dict = []
    with open('index.html', encoding='utf-8') as file:
        src = file.read()
    soup = BeautifulSoup(src, 'lxml')
    
    cards = soup.find_all('div', class_='wrapper')
    for item in cards:
        name = soup.find('div', class_='th').find('a').text
        
        if item.find('div', class_='price'):
            price = item.find('div', class_='price').text
        else:
            price = 'None'
        desc = item.find('div', class_='tovar').find('div', class_='text').text.replace('\n', '')
        company  = item.find('a', class_='personal_org_menu').text
        phone = item.find('a', class_='href_to_tel').text
        
        data = {
            'name': name,
            'description': desc,
            'price': price,
            'seller': company,
            'phone': phone
        }
        data_dict.append(data)
    with open('agroserver.json', 'w', encoding='utf-8') as file:
        json.dump(data_dict, file, indent=4, ensure_ascii=False)






def main():
    collect_data()

if __name__ == '__main__':
    main()
