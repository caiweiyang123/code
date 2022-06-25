# 1.3保存最后N个元素
# from collections import deque
# import heapq
#
# nums = [1, 4, 6, 7, 7, 9, 0, 4, 6, -5, 55]
# print(heapq.nlargest(2, nums))
# print(heapq.nsmallest(2, nums))

# 1.6在字典中将键值映射到多个值上
# from collections import defaultdict
#
# d = defaultdict(list)
# d['a'].append(1)
# d['a'].append(2)
# d['a'].append(3)
# d['b'].append(4)
# print(d)

# 1.8与字典有关的计算问题
# prices = {
#     "acme": 45.45,
#     "aapl": 304,
#     "IBM": 37.3,
#     "fb": 10.75,
# }
# min_price = min(zip(prices.values(), prices.keys()))
# prices_sorted = sorted(zip(prices.values(), prices.keys()), reverse=False)
# print(prices_sorted)

# 1.11 对切片命名
# record = '.........100......513.25.......'
# cost = int(record[9:12]) * float(record[18:24])
# print(cost)
# shares = slice(9, 12)
# price = slice(18, 24)
# cost = int(record[shares]) * float(record[price])
# print(cost)
# a =slice(0,50,2)
# # print(a.start)
# # print(a.stop)
# # print(a.step)
# s = "hello world"
# print(a.indices(len(s)))

# 1.12 找出序列中出现次数最多的元素
# from collections import Counter
#
# words = [1,3,4,5,7,8,9,0,6,4,2,5,7,8,2,3,4,5,6,7,8,9,1]
# s = "hello world"
# a = Counter(s)
# b = Counter(words)
# print(a)
# print(b)
# c = a+b
# print(c)
# top_three = c.most_common(3)
# print(top_three)

# 1.13通过公共键对字典列表排序
# rows = [
#     {"fname": "tom", "lname": "jones", "uid": 1002},
#     {"fname": "davis", "lname": "beadz", "uid": 1003},
#     {"fname": "john", "lname": "cless", "uid": 1004},
#     {"fname": "bing", "lname": "jones", "uid": 1001},
# ]
# from operator import itemgetter
#
# rows_by_fname  = sorted(rows,key=itemgetter('fname'))
# rows_by_uid = sorted(rows,key=itemgetter('uid'))
# print(rows_by_fname)
# print(rows_by_uid)

# # 1.15根据字段将记录分组
# rows = [
#     {"address": "5412", "date": "07/01/2012"},
#     {"address": "5232", "date": "05/01/2012"},
#     {"address": "5323", "date": "06/01/2012"},
#     {"address": "5423", "date": "07/01/2012"},
#     {"address": "5423", "date": "04/01/2012"},
#     {"address": "5453", "date": "05/01/2012"},
#     {"address": "5642", "date": "06/01/2012"},
# ]
# from operator import itemgetter
# from itertools import groupby
#
# rows.sort(key=itemgetter('date'))
#
# for date, items in groupby(rows, key=itemgetter('date')):
#     print(date)
#     for i in items:
#         print(" ", i)

#1.16筛选序列中的元素
# mylist = [1,2,4,6,8,-9,0,3,4,6,8,-1]
# a = [n for n in mylist if n >0]
# print(a)
# b = (n for n in mylist if n >0)
# # b = list(b)
# print(b)
# for i in b:
#     print(i,end='')

# 1.20将多个映射合并为单个映射
a = {"x":1,"z":3}
b = {"y":2,"z":4}
from collections import ChainMap
c = ChainMap(a,b)
print(c['z'])