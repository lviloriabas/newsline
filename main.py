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
entertainment = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=' \
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
        print(article.string + '\n')
        print(urljoin(url, article.get('href')) + '\n' * 2)


print("""Options:
t - Top stories
us - U.S. news
w - World news (excluding U.S.)
b - Business news
te - Technology news
e - Entertainment news
s - Sports news
sc - Science news
h - Health news
q - Quit
""")

while True:
    option = input('Choose an option: ')
    if option == 't':
        print('Top stories:')
        get_news(top)
    elif option == 'us':
        print('U.S. news')
        get_news(us)
    elif option == 'w':
        print('World news:')
        get_news(world)
    elif option == 'b':
        print('Business news:')
        get_news(business)
    elif option == 'te':
        print('Technology news:')
        get_news(technology)
    elif option == 'e':
        print('Entertainment news:')
        get_news(entertainment)
    elif option == 's':
        print('Sports news:')
        get_news(sports)
    elif option == 'sc':
        print('Science news:')
        get_news(science)
    elif option == 'h':
        print('Health news:')
        get_news(health)
    elif option == 'q':
        print('Quitting program.')
        break
    else:
        print('No option selected. Quitting program.')
        break
