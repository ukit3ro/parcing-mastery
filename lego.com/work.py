import requests
from bs4 import BeautifulSoup
import json

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
}


def get_links():
    r = requests.get(url='https://www.lego.com/en-us/themes', headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    links = []
    hrefs = soup.find('ul').find_all('li')
    for item in hrefs:
        links.append('https://www.lego.com' + item.find('a').get('href'))
    print(links)
    return links






def main():
    get_links()

if __name__ == "__main__":
    main()