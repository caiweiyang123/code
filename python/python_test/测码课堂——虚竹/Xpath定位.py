from selenium import webdriver
import time

# 加载驱动
driver = webdriver.Chrome()

# 打开网页
driver.get("https://www.baidu.com")

# 使用xpath定位到搜索框，打开输入关键字
# driver.find_element_by_xpath('//*[@id="kw"]').send_keys('长津湖')
driver.find_element_by_css_selector('.s_ipt').send_keys('长津湖')
