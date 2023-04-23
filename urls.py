import requests

from bs4 import BeautifulSoup


def get_news_urls():
    urls = []
    response = requests.get('https://news.google.com/home')

    soup = BeautifulSoup(response.content, 'html.parser')

    for link in soup.findAll('a', class_='WwrzSb'):
        urls.append(f"https://news.google.com{link.get('href')[1:]}")

    return urls
