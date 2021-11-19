import re

ret = re.match("嫦娥\d*号", "嫦娥112312号发射成功")
print(ret.group())

ret = re.match(".*", "嫦娥112312号发射成功")
print(ret.group())

ret = re.match(".+", "嫦娥112312号发射成功")
print(ret.group())

ret = re.match(".?", "嫦娥112312号发射成功")
print(ret.group())

ret = re.match("嫦娥\d{1,6}号", "嫦娥1125号发射成功")
print(ret.group())