from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
sleep(3)
driver.get("http://m.baidu.com")

# 参数数字为像素，宽480、高800，将浏览器设置成移动端大小
driver.set_window_size(480,800)

