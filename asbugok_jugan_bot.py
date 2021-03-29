#!/usr/bin/env python
# encoding=utf-8
import requests
import time
from bs4 import BeautifulSoup
import telegram

bot = telegram.Bot(token='1706220831:AAH8QhpdFL1KsMPhLuTHULDQAYY0WXguqlw')
if __name__ == '__main__':
    # 제일 최신 게시글의 번호 저장
    latest_num = 0
    req = requests.get(
        'http://www.asbugok.es.kr/board.list?mcode=272635&cate=272635')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    posts = soup.find("tr", {"class": "list1"})
    post_num = posts.find("td", {"class": "eng list_vspace"}).text

