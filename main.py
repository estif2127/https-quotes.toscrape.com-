import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
html = requests.get(url)


s = BeautifulSoup(html.content, 'html.parser')

authors = s.find_all('div', class_='col-md-8')
authors = s.find_all('small', class_='author')

for author in authors:
    print(author.text)
