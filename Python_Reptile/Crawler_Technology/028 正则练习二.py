import re

names = ["name1", "_111name", "2_name", "__name__"]

for name in names:
    r = re.match("[a-zA-Z_][\w]*", name)
    if r:
        print("变量名%s是有效的", r.group())
    else:
        print("变量名%s是无效的", name)
