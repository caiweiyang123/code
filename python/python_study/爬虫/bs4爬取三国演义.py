#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    # 对首页进行页面数据爬取
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
    url = "http://www.shicimingju.com/book/sanguoyanyi.html"
    page_text = requests.get(url=url, headers=headers)
    page_text.encoding = 'utf-8'
    page_text = page_text.text

    # 在首页中解析出章节的标题和详情页的url
    soup = BeautifulSoup(page_text, "lxml")
    # 解析章节标题和详情页url
    li_list = soup.select(".book-mulu > ul >li")
    fp = open('./三国演义.txt', "w", encoding='utf-8')
    for li in li_list:
        title = li.string
        detail_url = "https://www.shicimingju.com" + li.a['href']
        detail_page_url = requests.get(url=detail_url, headers=headers)
        detail_page_url.encoding = 'utf-8'
        detail_page_url = detail_page_url.text
        # 解析出详情页中相关的章节内容
        detail_soup = BeautifulSoup(detail_page_url, "lxml")
        div_tag = detail_soup.find('div', class_="chapter_content")
        # 解析到的章节内容
        content = div_tag.text
        fp.write(title + ":" + content + "\n")
        print(title, "爬取成功！！！")
