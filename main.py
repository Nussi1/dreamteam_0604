"""
Создать телеграм бот который читает данные из файла 'kloop.json'
И отправляет их к пользователю

Скинуть мне ссылку на телеграм бота для теста
"""


from requests.packages.urllib3.exceptions import InsecureRequestWarning
from bs4 import BeautifulSoup
import requests
import json

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

JSON = 'kloop.json'
HOST = 'https://kloop.kg/'
URL = 'https://kloop.kg/news/'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
}

def get_content():
    r = requests.get(url=URL, headers=HEADERS, verify=False)
    soup = BeautifulSoup(r.text, 'html.parser')
    items = soup.findAll('article', class_='elementor-post')

    new_posts = []

    for item in items:
        new_posts.append({
            'title': item.find('h3', class_ = 'elementor-post__title').get_text(strip=True),
             'link_news': item.find('h3', class_='elementor-post__title').find('a').get('href'),
             'date': item.find('div', class_='elementor-post__meta-data').get_text(strip=True),
             'photo': item.find('div', class_='elementor-post__thumbnail').find('img').get('src'),
        })

    with open('kloop.json', 'w') as file:
        json.dump(new_posts, file, indent=4, ensure_ascii=False)


def main():
    get_content()

if __name__ == "__main__":
    main()