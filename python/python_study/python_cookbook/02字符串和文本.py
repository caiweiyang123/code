#2.1针对任意多的分割符拆分字符串
# line = "asdf fjsk; afsdf, asda,sadw,asad,  foo"
# import re
# res = re.split(r"[;,\s]\s*",line)
# print(res)
# res = re.split(r"(;|,|\s)\s*",line)
# print(res)

# 2.4文本模式的匹配和查找
# text1 = "11/27/2012"
# text2 = "NOV 27, 2012"
# import re
# datepat = r"\d+/\d+/\d+"
# if re.match(datepat,text1):
#     print("yes")
# else:
#     print("no")
#
# if re.match(datepat,text2):
#     print("yes")
# else:
#     print("no")
#
# text = "Today is 11/27/2012 . PyCon starts 3/13/2013"
# res = re.findall(datepat,text)
# print(res)

# 引入捕获组
# import re
#
# datepat = re.compile("(\d+)/(\d+)/(\d+)")
# m = datepat.match("11/27/2012")
# # print(m.groups())
# text = "Today is 11/27/2012 . PyCon starts 3/13/2013"
# res = datepat.findall(text)
# # print(res)
# for month,day,year in datepat.findall(text):
#     print(f"{month}-{day}-{year}")
#
# for m in datepat.finditer(text):
#     print(m.groups())

# 2.5查找和替换文本
# text = "Today is 11/27/2012 . PyCon starts 3/13/2013"
# import re
# res = re.sub(r"(\d+)/(\d+)/(\d+)",r"\3-\1-\2",text)
# print(res)
#
# from calendar import month_abbr
# def change_date(m):
#     mon_name = month_abbr[int(m.group(1))]
#     return f"{m.group(2)}-{mon_name}-{m.group(3)}"
#
# datepat = re.compile(r"(\d+)/(\d+)/(\d+)")
# result = datepat.sub(change_date(datepat),text)
# print(result)

#2.8多行模式的正则表达式
# import re
#
# import requests
#
# text = """
#     /* this is a
# multiline comment */
# """
# comment = re.compile(r"/\*((?:.|\n)*?)\*/")
# res = comment.findall(text)
# print(res)

# 2.14字符串链接以及合并
data = ["ace",20,91.1]
# result = ",".join(data) #TypeError: sequence item 1: expected str instance, int found
result = ",".join(str(item) for item in data)
print(result)