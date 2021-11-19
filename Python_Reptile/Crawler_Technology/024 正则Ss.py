import re

ret = re.match("\s\s\spython", "   python")
print(ret.group())

ret = re.match("\S\Spython", "aspython")
print(ret.group())
