import re

# r = re.findall("1[0-9]{10}","张三：15850162469")
# print(r)
# s = "321323199306100633"
# r = re.search(r"\d{17}(\d|x)",s).group()
# print(r)

r = dir(re)
print(r)
pattern = "asdsdas"
regex = complex(pattern, flags=0)
# # 练习1 匹配一个.com邮箱格式字符串
# s1 = "invest_cai@163.com"
# print(re.findall(r"\w+@\w+.com$", s1))
# # 练习2 匹配一个密码 8-12位数字字母下划线构成
# s2 = "Qiu601_872Q2"
# print(re.findall(r"^\w{8,12}$", s2))
# # 练习3 匹配一个数字，正数，负数，整数，小数，分数1/2,百分数45%
# s3 = "28 -48 15 1/2 2.8 -45.8 34% 23.3% fs 123 sdsfs 22312312.2132"
# print(re.findall(r"-?\d+\.?\/?\d+%?", s3))
# # 练习4 匹配一段文字中以大写字母开头的单词，注意文字中可能有IPython（不算） H-base（算）
# #  单词可能有 大写字母 小写字母 - _
# s4 = "Aasd  Tsev dscse I sdFf hos Hsd IPthon H-base Ja_me sdjo SD DEd"
# print(re.findall(r"\b[A-Z][-_a-z]+",s4))
