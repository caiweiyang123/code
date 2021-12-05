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

# 生成match函数
s = "今年是2019年，建国70周年"
pattern = r"\d+"

it=re.finditer(pattern,s)
for item in it:
    print(item.group()) # 获取match对象对应内容

# 完全匹配一个字符串
s = "今年是2019年，建国70周年"
m = re.fullmatch(r"[，\w]+",s)
print(m.group())

# 匹配字符串开始位置
m =re.match(r"\w+",s)
print(m.group())

# 匹配第一处符合正则规则的内容
m = re.search(r'\d+',s)
print(m.group())

# 捕获组的用法
regex = re.compile(r"(ab)cd(?P<name>ef)")

print(regex.flags)
print(regex.pattern)
print(regex.groupindex)
print(regex.groups)


pattern = r"(?P<DOG>ab)cd(?P<name>ef)"
regex = re.compile(pattern)
obj = regex.search("abcdefghijk")

# 属性变量
print(obj.pos) # 目标字符串开始的位置
print(obj.endpos) # 目标字符串结束位置
print(obj.re) # 正则
print(obj.string) # 目标字符串
print(obj.lastgroup) # 最后一组组名
print(obj.lastgroup) # 最后一组序列号
print(obj.lastindex) # 最后一组序列号

print("="*50)
# 属性方法
print(obj.span())
print(obj.start())
print(obj.end())
print(obj.groupdict())
print(obj.groups())
print(obj.group())
print(obj.group("name"))