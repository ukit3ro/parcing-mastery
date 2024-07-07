from bs4 import BeautifulSoup
import json


with open('index0.html') as file:
    src = file.read()
soup = BeautifulSoup(src, 'lxml')

cards = soup.find_all('div', class_='card')
data_dict = []

for item in cards:
    name = item.find('a').get('title')
    details = item.find_all('p', class_='details-list')
    detlist = []
    for p in details:
        spans = p.find_all('span')
        for s in spans:
            if s.text.strip() is not None and s.text != '':
                detlist.append(s.text)
    link = 'https://celebrations.com' + item.find('a', class_= 'card-details-link').get('href')
    data = {
        'name': name,
        'link': link,
        'details': detlist
    }
    data_dict.append(data)

with open('festivos.json', 'w') as file:
    json.dump(data_dict, file, indent=4, ensure_ascii=False)
    
