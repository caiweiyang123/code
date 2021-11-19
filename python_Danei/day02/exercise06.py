"""
    模块的练习
"""
# 练习1：完成
# 练习2：（1）
"""
list01 = [
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"]
]
"""
from python_Danei.day01.demo03 import list01
import double_list_helper as d01

num01 = d01.DoubleListHelper.get_elements(list01,d01.Vector2(1,3),d01.Vector2.left(),3)
num02 = d01.DoubleListHelper.get_elements(list01,d01.Vector2(2,2),d01.Vector2.up(),2)
num03 = d01.DoubleListHelper.get_elements(list01,d01.Vector2(0,3),d01.Vector2.down(),2)
print(num01)
print(num02)
print(num03)