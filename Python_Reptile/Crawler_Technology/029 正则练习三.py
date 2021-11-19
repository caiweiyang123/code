import re

# 匹配出。0到99之间的数字

r = re.match("[1-9]?[0-9]","17")
print(r.group())