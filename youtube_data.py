from urllib import request
import urllib.request
from bs4 import BeautifulSoup


open_HTML_file = open("C:\\Users\\user\\Desktop\\project 3\\Takeout\\YouTube and YouTube Music\\history\\watch-history.html", 'r', encoding='utf8')
contents = open_HTML_file.read()
beautifulsoupText = BeautifulSoup(contents, 'lxml')
info = beautifulsoupText.find_all('div', class_='outer-cell mdl-cell mdl-cell--12-col mdl-shadow--2dp')
for index, option in enumerate(info):
    watched = option.find('div', class_='content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1').text
    dateTime = watched[-23:].strip()
    with open('C:\\Users\\user\\Desktop\\project 3\\watch_history.txt', 'a') as f:
        f.write(f'{dateTime}\n')
    if dateTime not in open('C:\\Users\\user\\Desktop\\project 3\\watch_history.txt', 'r'):
        open('C:\\Users\\user\\Desktop\\project 3\\watch_history.txt', 'a')
          #f.write(f'{dateTime}\n')
    print(f'saved: {index}')
