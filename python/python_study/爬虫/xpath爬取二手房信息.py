#!/usr/bin/env python
# -*- coding:utf-8 -*-
from lxml import etree
import requests

# 需求：爬取58同城二手房的房源信息
if __name__ == '__main__':
    # 爬取页面源码数据
    url = "https://sh.58.com/ershoufang/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
    page_text = requests.get(url=url, headers=headers).text
    # 数据解析
    # 实例化一个etree对象，且将被解析的文本加载到对象中
    tree = etree.HTML(page_text)
    div_list = tree.xpath('//section[@class="list"]/div')
    print(div_list)
    fp = open('58.txt', "w", encoding='utf-8')
    for div in div_list:
        title = div.xpath('.//div[@class="property-content-title"]/h3/text')[0]
        print(title)
        fp.write(title+"\n")
