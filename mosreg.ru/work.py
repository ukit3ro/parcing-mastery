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



def collect_list():
    museis = []
    for i in range(1,17):
        req = requests.get(f'https://welcome.mosreg.ru/places/museums?page={i}&per-page=12', headers=headers)
        soup = BeautifulSoup(req.text, 'lxml')
        links = soup.find_all('a', class_='w_newsList__item-box')
        for link in links:
            museis.append('https://welcome.mosreg.ru' + link.get('href'))
    with open('museum_list.txt', 'a') as file:
        for line in museis:
            file.write(f'{line}\n')


def collect_data():
    with open('museums_list.txt') as file:
        lines = [line.strip() for line in file.readlines()]
        data_dict = []
        
        for line in lines:
            q = requests.get(line, headers=headers)
            soup = BeautifulSoup(q.content, 'lxml')

            name = soup.find('h1').text
            
            if soup.find('div', class_='rs-one-distance') is not None:
                distance = soup.find('div', class_='rs-one-distance').find('span').text
            else:
                distance = 'None'
            print(name)

            info_block = soup.find('div', class_='rs-three-left sticky-sidebar').find('ul').find_all('li')
            adress = info_block[0].find('a').text.replace('"', '').replace('\n', '').strip()
            
            if len(info_block) >=3:
                contacts_bl = info_block[2].find_all('a')
            else:
                contacts_bl = info_block[1].find_all('a')
            contacts  = []
            contacts.append(contacts_bl[0].text.replace('"', '').replace('\n', '').strip())
            if len(contacts_bl) >= 2:
                contacts.append(contacts_bl[1].get('href'))
            if len(contacts_bl) >= 3:
                contacts.append(contacts_bl[2].get('href'))
            if len(contacts_bl) >= 4:
                contacts.append(contacts_bl[3].get('href'))
            
            data = {
                'name': name,
                'distance': distance,
                'adress': adress,
                'contacts': contacts,
            }
            data_dict.append(data)
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data_dict, json_file, indent=4, ensure_ascii=False)
            


def main():
    collect_data()

if __name__ == '__main__':
    main()