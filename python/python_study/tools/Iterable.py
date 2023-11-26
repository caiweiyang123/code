# 可迭代的对象：1。生成器（直接又是迭代器） 2.元组 列表 集合 字典 字符串（需要借助iter（）函数转化成迭代器）
# 如何判断一个对象是否是可迭代？
from collections import Iterable

list1 = [1, 2, 3, 4, 5]
f = isinstance(list1, Iterable)
print(f)
f = isinstance("list1", Iterable)
print(f)
f = isinstance(100, Iterable)
print(f)

# 可以用iter（）把可迭代的变成迭代器
