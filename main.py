from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

top = 'https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en'
us = 'https://news.google.com/topics/CAAqIggKIhxDQkFTRHdvSkwyMHZNRGxqTjNjd0VnSmxiaWdBUAE?hl=en-US&gl=US&ceid=US%3Aen'
world = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=' \
        'US&ceid=US%3Aen'
business = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=' \
           'US&ceid=US%3Aen'
technology = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=' \
             'US&ceid=US%3Aen'
sports = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=' \
         'US&ceid=US%3Aen'
science = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp0Y1RjU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=' \
          'US&ceid=US%3Aen'
health = 'https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNR3QwTlRFU0FtVnVLQUFQAQ?hl=en-US&gl=US&ceid=US%3Aen'

news_limit = 6


def get_news(url):

    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    articles = soup.find_all('a', class_='DY5T1d RZIKme', limit=news_limit)

    for article in articles:
        print(article.string)
        print(urljoin(url, article.get('href')))


get_news(top)
