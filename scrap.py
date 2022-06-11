import requests
import bs4
from fake_headers import Headers

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

url = 'https://habr.com/ru/all/'
header = Headers()
gen = header.generate()

response = requests.get(url, headers=gen)
result = response.text

soup = bs4.BeautifulSoup(result, features='html.parser')

articles = soup.find_all("article")

for article in articles:
    art_bod = article.find_all(class_="article-formatted-body")
    art_bod = [art.text.strip() for art in art_bod]
    for art_word in art_bod:
        for word in KEYWORDS:
            if word in art_word:
                date = article.find(class_="tm-article-snippet__meta").find("time")
                head = article.find("h2").find("span")
                href = article.find(class_="tm-article-snippet__title-link").attrs["href"]

                print(f"{date.text} {head.text} https://habr.com/ru/all{href}")
