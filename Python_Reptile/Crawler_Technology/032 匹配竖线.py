import re

# 匹配出163、126、qq邮箱，且@符号之前有4到20位，必须是字母开头

r = re.match("[a-zA-Z]\w{3,19}@163\.com", "hello@163.com")
print(r.group())

r = re.match("[a-zA-Z]\w{3,19}@163\.com|[a-zA-Z]\w{3,19}@126\.com|[a-zA-Z]\w{3,19}@qq\.com", "hello@qq.com")
print(r.group())

r = re.match("[a-zA-Z]\w{3,19}@(163|126|qq)\.com", "hello@163.com")
print(r.group())