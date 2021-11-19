import re
#匹配出.8到20位的密码，可以是大小写英文字母、数字下划线

r = re.match("[a-zA-Z0-9_]{8,20}","asdad28ad9ad8")
print(r.group())

r = re.match("[\w]{8,20}","asdad28ad9ad8")
print(r.group())