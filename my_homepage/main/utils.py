import requests
from bs4 import BeautifulSoup

# 네이버뉴스 타이틀을 크롤링해서 리스트객체로 반환
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
