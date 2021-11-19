import re

# 使用match方法进行匹配操作
res = re.match('h...o', 'hello world')

# 如果上面匹配到数据的话，可以使用group放大来提取
print(res.group())

res = re.match('t.o', 'too')
print(res.group())