"""
    练习：
        在控制台输入一个四位数：1234
        计算每位相加的和
        显示结果
"""
# 第一种方法
# number = int(input("请输入一个四位数："))
# unit01 = number % 10
# unit02 = number // 10 % 10
# unit03 = number // 100 % 10
# unit04 = number // 1000
# result = unit01+unit02+unit03+unit04
# print("结果是：%d"%(result))

# 第二种方法
number = int(input("请输入一个四位数："))
result = number % 10
result += number // 10 % 10
result += number // 100 % 10
result += number // 1000
print("结果是：%d" % (result))
