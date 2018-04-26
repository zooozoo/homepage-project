import requests
from bs4 import BeautifulSoup


def naver_news_title():
    req = requests.get('http://news.naver.com/main/home.nhn')
    html = req.text
    soup = BeautifulSoup(html, 'lxml')
    today_main = soup.find('div', id='pan_today_main_news')

    result = []
    for item in today_main.find_all('li'):
        if len(item.a.text) < 3:
            continue
        string = item.a.text
        link = item.a.get('href')
        tu = ('naver', string, link)
        result.append(tu)
    return result


def daum_news_title():
    req = requests.get('http://media.daum.net/')
    html = req.text
    soup = BeautifulSoup(html, 'lxml')
    total_list = soup.find('div', class_='box_headline')

    result = []
    for item in total_list.find_all('a', class_='link_txt')[0:10]:
        string = item.text.strip()
        link = item.get('href')
        tu = ('daum', string, link)
        result.append(tu)
    return result


def chosun_news_title():
    req = requests.get('http://www.chosun.com/')
    html = req.content.decode('euc-kr', 'replace')
    soup = BeautifulSoup(html, 'lxml')
    news_section = soup.find(class_='sec_con')

    result = []
    top_news = news_section.find('div', id='top_news').h2
    top_news_tu = (
        'chosun',
        top_news.find('em').text + '\n' + top_news.find('em').next_sibling.text,
        top_news.find('a').get('href')
    )
    second_news = news_section.find('dl', id='second_news')
    second_news_tu = ('chosun', second_news.dt.text, second_news.a.get('href'))
    result.append(top_news_tu)
    result.append(second_news_tu)
    for item in news_section.find_all('dl', class_='art_list_item')[0:8]:
        string = item.dt.a.text
        link = item.dt.a.get('href')
        tu = ('chosun', string, link)
        result.append(tu)
    return result


def all_crawler_function():
    return naver_news_title() + daum_news_title() + chosun_news_title()
