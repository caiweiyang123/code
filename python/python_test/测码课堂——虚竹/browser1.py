from selenium import webdriver
from time import sleep
"""
back() 后退 
forward()前进
refresh()刷新
"""
driver = webdriver.Chrome()

first_url = 'http://www.baidu.com'
print('进入页面%s'%(first_url))
driver.get(first_url)
sleep(2)

# 访问新闻页面
second_url = 'http://news.baidu.com'
print('进入页面%s'%(second_url))
driver.get(second_url)
sleep(2)

# 返回到百度首页
print('返回到百度首页%s'%first_url)
driver.back()
sleep(2)

# 前进至新闻页面
print('前进至新闻页面%s'%second_url)
driver.forward()
sleep(2)

# 刷新页面
print('刷新当前页面%s'%second_url)
driver.refresh()
