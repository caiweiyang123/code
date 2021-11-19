import re

ret = re.match("[a-zA-Z]", "Bpython")
print(ret.group())

ret = re.match("\d\dpython", "12python")
print(ret.group())

ret = re.match("\d\Dpython", "1spython")
print(ret.group())