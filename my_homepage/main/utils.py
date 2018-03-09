import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.naver.com/')
html = req.text
print(html)