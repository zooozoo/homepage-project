import requests
from bs4 import BeautifulSoup


def naver_news_title():
    req = requests.get('http://news.naver.com/main/home.nhn')
    html = req.text
    soup = BeautifulSoup(html, 'lxml')

    result = []
    for item in soup.find_all('a', class_='nclicks(hom.headcont)'):
        if item.string:
            string = item.string
            link = item.get('href')
            tu = (string, link)
            result.append(tu)
    return result


def daum_news_title():
    req = requests.get('http://media.daum.net/')
    html = req.text
    soup = BeautifulSoup(html, 'lxml')
    total_list = soup.find_all('div', 'box_headline')[0]

    result = []
    for item in total_list.find_all('a', 'link_txt'):
        string = item.string.strip()
        link = item.get('href')
        tu = (string, link)
        result.append(tu)
    return result