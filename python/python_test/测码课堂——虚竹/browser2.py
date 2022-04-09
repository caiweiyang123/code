"""
clear() 清除文本
send_keys(*value) 模拟键盘输入
click()  单击元素
size 返回元素的尺寸
text 获取元素的文本
get_attribute(name) 获取元素属性
is_displayed() 该元素是否用户可见
"""
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

# 模拟键盘输入
search_text = driver.find_element_by_id('kw')
sleep(2)

# # 单击元素
# driver.find_element_by_id('su').click()
# sleep(2)
#
# # 清除文本
# driver.find_element_by_id('kw').clear()
# sleep(2)

# submit 提交表单，模拟回车键
search_text.send_keys('长津湖')
search_text.submit()