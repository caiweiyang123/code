import requests
# 需求：爬取梨视频的视频数据
from lxml import etree

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
# 原则：线程池处理的是阻塞并耗时的数据

# 对下述url发起请求解析出视频详情页的url和
url = "https://www.pearvideo.com/category_5"
page_text = requests.get(url=url,headers=headers).text

tree = etree.HTML(page_text)
li_list = tree.xpath('//*[@id="listvideoListUl"]/li')
