import re

ret = re.match("\w\w\wpython", "3p_python")
print(ret.group())

ret = re.match("\w\w\Wpython", "3p@python")
print(ret.group())
