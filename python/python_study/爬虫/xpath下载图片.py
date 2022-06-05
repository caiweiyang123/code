#!/usr/bin/env python
# -*- coding:utf-8 -*-
from lxml import etree
import requests
import os

# 需求：爬取58同城二手房的房源信息
if __name__ == '__main__':
    # 爬取页面源码数据
    url = "https://pic.netbian.com/4kmeinv/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
    page_text = requests.get(url=url, headers=headers).text
    # page_text.encoding = 'utf-8'
    # page_text = page_text.text
    # 数据解析
    tree = etree.HTML(page_text)
    li_list = tree.xpath("//div[@class='slist']/ul/li")

    # 创建一个文件夹
    if not os.path.exists('./piclibs'):
        os.mkdir('./piclibs')

    for li in li_list:
        img_src = "https://pic.netbian.com" + li.xpath("./a/img/@src")[0]
        img_name = li.xpath("./a/img/@alt")[0] + '.jpg'
        img_name = img_name.encode('iso-8859-1').decode('gbk')
        # print(img_name, img_src)

        # 持久化存储
        img_data = requests.get(url=img_src, headers=headers).content
        img_path = 'piclibs/' + img_name
        with open(img_path, 'wb') as fp:
            fp.write(img_data)
            print(img_name, "下载成功！")
