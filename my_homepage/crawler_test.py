import re

import requests
from bs4 import BeautifulSoup

# script처럼 test 해보기 위한 setting
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from main.models import NewsTitle


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
        tu = NewsTitle(pres='naver', title=string, link=link)
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
        tu = NewsTitle(pres='daum', title=string, link=link)
        result.append(tu)
    return result


def chosun_news_title():
    req = requests.get('http://www.chosun.com/')
    html = req.content.decode('euc-kr', 'replace')
    soup = BeautifulSoup(html, 'lxml')
    news_section = soup.find(class_='sec_con')

    result = []
    # top news
    top_news = news_section.find('div', id='top_news')
    if not top_news:
        news_section = soup.find('section', id='sec_headline')
        top_news = news_section.find_all('a', onclick="ga('send', 'event', 'Headline', 'news', 'Top');")[0]
        top_news_tu = NewsTitle(
            pres='chosun',
            title=top_news.text,
            link=top_news.get('href')
        )
    else:
        top_news_tu = NewsTitle(
            pres='chosun',
            title=top_news.find('h2').text,
            link=top_news.find('a').get('href')
        )
    result.append(top_news_tu)

    # second_news
    second_news = news_section.find('dl', id='second_news')
    second_news_tu = NewsTitle(
        pres='chosun',
        title=second_news.dt.text,
        link=second_news.a.get('href')
    )
    result.append(second_news_tu)

    # main_news
    for item in news_section.find_all('dl', class_='art_list_item')[0:8]:
        string = item.dt.a.text
        link = item.dt.a.get('href')
        tu = NewsTitle(pres='chosun', title=string, link=link)
        result.append(tu)
    return result


def joongang_news_title():
    req = requests.get('http://joongang.joins.com/')
    html = req.content
    soup = BeautifulSoup(html, 'lxml')

    result = []
    # hot뉴스
    hot_article_section = soup.find(
        'div',
        longdesc='joongang:15re_home_showcase:showcase_type_top_news:1:Top news type'
    )
    if hot_article_section:
        for item in hot_article_section.find_all('div', class_='text_area'):
            string = item.find('span', class_='text_center').a.text.replace('\xa0', '')
            link = item.find('span', class_='text_center').a.get('href')
            tu = NewsTitle(pres='joongang', title=string, link=link)
            result.append(tu)
    else:
        # 위의 hot뉴스 없을 경우 today's hot 가져오는 로직
        hot_article_section = soup.find(
            'div',
            class_='todays_hot'
        )

        tu = NewsTitle(
            pres='joongang',
            title=hot_article_section.find('span', class_='text_wrap').a.text,
            link=hot_article_section.find('span', class_='text_wrap').a.get('href'),
        )
        result.append(tu)

    # main_news
    main_article_section = soup.find('div', class_='clt')
    for item in main_article_section.find_all('strong', class_='headline')[:10]:
        string = item.text
        link = item.a.get('href')
        tu = NewsTitle(pres='joongang', title=string, link=link)
        result.append(tu)
    return result[:10]


def donga_news_title():
    req = requests.get('http://www.donga.com/')
    html = req.content
    soup = BeautifulSoup(html, 'lxml')

    result = []

    # top_news
    head_title_news = soup.find('div', class_='head_title')
    tu = NewsTitle(pres='donga', title=head_title_news.a.text, link=head_title_news.a.get('href'))
    result.append(tu)

    # main_news
    main_news = soup.find('div', class_='mNewsLi')
    for item in main_news.find_all('a')[:15]:
        if item.text is '' or len(item.text) > 40:
            continue
        string = item.text
        link = item.get('href')
        tu = NewsTitle(pres='donga', title=string, link=link)
        result.append(tu)
    return result[:10]


# 한겨레
def hani_news_title():
    req = requests.get('http://www.hani.co.kr/')
    html = req.content
    soup = BeautifulSoup(html, 'lxml')

    result = []
    # top new
    top_news_section = soup.find(class_='article-title')
    tu = NewsTitle(
        pres='hani',
        title=top_news_section.a.text,
        link='http://www.hani.co.kr' + top_news_section.a.get('href')
    )
    result.append(tu)

    # main news
    main_news_section = soup.find('div', class_='main-top01')
    for item in main_news_section.find_all(class_='article-title')[:9]:
        string = item.a.text
        link = item.a.get('href')
        tu = NewsTitle(pres='hani', title=string, link='http://www.hani.co.kr' + link)
        result.append(tu)
    return result


def ohmy_news_title():
    req = requests.get('http://www.ohmynews.com/')
    html = req.content
    soup = BeautifulSoup(html, 'lxml')

    result = []

    # top news
    top_section = soup.find('div', id='top_area')
    for item in top_section.find_all(class_='titl'):
        string = item.a.text
        link = 'http://www.ohmynews.com' + item.a.get('href')
        tu = NewsTitle(pres='ohmy', title=string, link=link)
        result.append(tu)

    # main news
    main_section = soup.find('div', class_='list_unit')
    for item in main_section.find_all('a', onclick="GA_Event('메인_기사', '으뜸_클릭');")[:8]:
        if item.text is '':
            continue
        string = item.text
        link = 'http://www.ohmynews.com' + item.get('href')
        tu = NewsTitle(pres='ohmy', title=string, link=link)
        result.append(tu)
    return result[:10]


def khan_news_title():
    # session = requests.Session()
    # session.max_redirects = 200
    # req = session.get('http://www.khan.co.kr/')
    # html = req.content
    # soup = BeautifulSoup(html, 'lxml')

    # session을 사용하지 않고도 되는지 test
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'
    headers = {'User-Agent': user_agent}
    req = requests.get('http://www.khan.co.kr/', headers=headers)
    html = req.content
    soup = BeautifulSoup(html, 'lxml')

    result = []
    # top news
    top_news_tu = NewsTitle(
        pres='khan',
        title=soup.find('div', class_='topNews').a.text,
        link=soup.find('div', class_='topNews').a.get('href')
    )
    result.append(top_news_tu)

    # head line
    head_line = soup.find('div', class_='mArticle')
    head_line_tu = NewsTitle(
        pres='khan',
        title=head_line.find('div', class_='textArea').a.text.replace('\xa0', ''),
        link=head_line.find('div', class_='textArea').a.get('href'),
    )
    result.append(head_line_tu)

    # head line2
    head_line2 = soup.find('div', class_='sArticle')
    for item in head_line2.find_all('a'):
        string = item.text.replace('\xa0', '')
        link = item.get('href')
        tu = NewsTitle(pres='khan', title=string, link=link)
        result.append(tu)

    # main
    main_title = soup.find('div', class_='clt')
    for item in main_title.find_all(class_='hd_title')[:4]:
        string = item.a.text.replace('\xa0', '')
        link = item.a.get('href')
        tu = NewsTitle(pres='khan', title=string, link=link)
        result.append(tu)
    return result


def kbs_news_title():
    req = requests.get('http://news.kbs.co.kr/common/main.html')
    html = req.content
    soup = BeautifulSoup(html, 'lxml')

    result = []
    # 구조가 아예 바뀐건지 확인할 수 없기에 주석처리로 임시 대기
    # # top news
    # top_news = soup.find('div', class_='headline_top')
    # for item in top_news.find_all('li'):
    #     string = item.img['alt']
    #     link = 'http://news.kbs.co.kr' + item.a.get('href')
    #     tu = NewsTitle(pres='kbs', title=string, link=link)
    #     result.append(tu)
    #
    # # head lines
    # head_line = soup.find('div', class_='headline_blk_list1')
    # for item in head_line.find_all('a')[:7]:
    #     string = item.text.strip()
    #     link = 'http://news.kbs.co.kr' + item.get('href')
    #     tu =NewsTitle(pres='kbs', title=string, link=link)
    #     result.append(tu)

    top_news = soup.find('div', class_='section-box')
    for item in top_news.find_all('a'):
        string = re.sub('\s+', ' ', item.em.text.strip())
        link = 'http://news.kbs.co.kr' + item.get('href')
        tu = NewsTitle(pres='kbs', title=string, link=link)
        result.append(tu)

    head_line = soup.find('div', class_='m-section main-topnews').find('ul', class_='list-type list-text')
    for item in head_line.find_all('li'):
        string = item.text.strip()
        link = 'http://news.kbs.co.kr' + item.a.get('href')
        tu = NewsTitle(pres='kbs', title=string, link=link)
        result.append(tu)
    return result[:10]


def sbs_news_title():
    req = requests.get('https://news.sbs.co.kr/news/newsMain.do?div=pc_news')
    html = req.content
    soup = BeautifulSoup(html, 'lxml')

    result = []
    # top news
    for item in soup.find('div', class_='head_inner').find_all('li'):
        string = item.a.text.strip()
        link = item.a.get('href')
        tu = NewsTitle(pres='sbs', title=string, link='https://news.sbs.co.kr' + link)
        result.append(tu)

    # 오늘의 기사
    result.append(NewsTitle(
        pres='sbs',
        title=soup.find('div', class_='w_side_list').a.p.text.strip(),
        link='https://news.sbs.co.kr' + soup.find('div', class_='w_side_list').a.get('href')
    ))

    # hot news
    hot_art_section = soup.find('div', class_='hot_area')
    for item in hot_art_section.find_all('li')[:5]:
        string = re.sub('\s+', ' ', item.a.text.strip())
        link = 'https://news.sbs.co.kr' + item.a.get('href')
        tu = NewsTitle(pres='sbs', title=string, link=link)
        result.append(tu)
    return result


def mbc_news_title():
    req = requests.get('http://imnews.imbc.com/index_pc.html')
    html = req.content
    soup = BeautifulSoup(html, 'lxml')

    result = []
    # main top 3개
    # main_top_section의 url http://imnews.imbc.com/mmain/headline/index.js
    main_top_section = soup.find('div', class_='main_top').find('script')['src']
    main_top_req = requests.get(main_top_section)
    main_top_soup = BeautifulSoup(main_top_req.content, 'lxml')

    for item in main_top_soup.find_all('li'):
        string = item.a.text.replace('\\', '').strip()
        link = item.a.get('href')
        tu = NewsTitle(pres='mbc', title=string, link=link)
        result.append(tu)

    # main news 6개
    main_req = requests.get('http://imnews.imbc.com/mmain/default/index.js')
    main_soup = BeautifulSoup(main_req.content, 'lxml')
    for item in main_soup.find_all('a', class_='alt_1_detail_link'):
        string = item.text.replace('\\', '')
        link = item.get('href')
        tu = NewsTitle(pres='mbc', title=string, link=link)
        result.append(tu)
    return result


def all_crawler_collect():
    return naver_news_title() + daum_news_title() + chosun_news_title() \
           + joongang_news_title() + donga_news_title() + hani_news_title() \
           + ohmy_news_title() + khan_news_title() + kbs_news_title() + \
           sbs_news_title() + mbc_news_title()


