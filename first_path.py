import re
from bs4 import BeautifulSoup

with open('index.html') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')

title = soup.title


page_h1 = soup.find('h1')

page_all_h1 = soup.find_all('h1')
""" print(page_all_h1) """

user_name = soup.find(class_='user__name').find('span').text
""" print(user_name) """




""" social_links = soup.find(class_='social__networks').find('ul').find_all('a')

all_a = soup.find_all('a')
for item in all_a:
    item_text = item.text
    item_url = item.get('href')
    print(f'{item_text}: {item_url}') """
    

""" post_div = soup.find(class_='post__text').find_parent('div', 'user__post')
print(post_div)

post_divs = soup.find(class_='post__text').find_parents('div', 'user__post')
print(post_divs) """




""" next_el = soup.find(class_='post__title').find_next().text
print(next_el) """


""" next_sib = soup.find(class_='post__title').find_next_sibling()
print(next_sib) """

""" links = soup.find(class_='some__links').find_all('a')

for link in links:
    link_href_attr = link.get('href')
    link_href_attr1 = link['href']
    
    link_data_attr = link.get('data-attr') """
    




