import requests
from bs4 import BeautifulSoup

def naver_news_title():
    req = requests.get('http://news.naver.com/main/home.nhn')
    html = req.text
    soup = BeautifulSoup(html, 'lxml')
    result = []
    for item in soup.find_all('a', class_='nclicks(hom.headcont)'):
        if item.string:
            s = item.string
            result.append(s)
    return result

for i in naver_news_title():
    print(i)