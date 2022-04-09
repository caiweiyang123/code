import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.baidu.com/')
# 查找元素并输入
driver.find_element('id', 'kw').send_keys("长津湖")
# 查找元素并点击
driver.find_element_by_id('su').click()
time.sleep(2)
assert "长津湖" in driver.title

# 关闭浏览器
driver.quit()
