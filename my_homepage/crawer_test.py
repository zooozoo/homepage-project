import requests
from bs4 import BeautifulSoup

def naver_news_title():
    req = requests.get('http://news.naver.com/main/home.nhn')
    html = req.text
    soup = BeautifulSoup(html, 'lxml')
    total_list = soup.find_all('div', id='pan_today_main_news')[0]
    result = []
    for i in total_list.find_all('div', 'newsnow_tx_inner'):
        if len(i['class']) == 2:
            continue
        result.append(i.a.string)
    return result


def daum_news_title():
    req = requests.get('http://media.daum.net/')
    html = req.text
    soup = BeautifulSoup(html, 'lxml')
    total_list = soup.find_all('div', 'box_headline')[0]
    result = []
    for i in total_list.find_all('a', 'link_txt'):
        result.append(i.string.strip())
    return result
