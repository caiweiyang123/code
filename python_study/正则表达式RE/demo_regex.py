"""
    regex.py re模块 功能演示
"""
import re

# 目标字符串
s = "Alex:1994,Sunny:1996"
pattern = r"\w+:\d+" #正则表达式

# re模块调用findall
r = re.findall(pattern,s,flags=0)
print(r)

# compile 对象调用findall
regex = re.compile(pattern)
r = regex.findall(s,0,10)
print(r)

# 按照正则表达式匹配内容切割字符串split
r = re.split(r"[:,]",s)
print(r)

# sub替换目标字符串
s = re.subn(r":","-",s)
print(s)