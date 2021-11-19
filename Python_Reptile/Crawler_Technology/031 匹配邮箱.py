import re

# 匹配出163邮箱地址，且@符号之前有4到20位，例如hello@163.com

# r = re.match(".{4,20}@163.com", "hello@163.com")
# print(r.group())

email_list = ["haha@163.com", "haha@163.comads", ".asw.ss@qq.com"]

for email in email_list:
    r = re.match(".{4,20}@163\.com$", email)
    if r:
        print("%s是符合规定的邮件地址" % (r.group()))
    else:
        print("%s是不符合规定的邮件地址" % email)
