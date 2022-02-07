"""
    计算机基础
        -数据结构
        -操作系统
        -计算机组成原理
        -网络基础
"""
# 异常处理
# 什么是异常？）
# 异常是程序发生错误的信号，程序一旦出错就会抛出异常，程序的运行就终止了

# 异常的三个特征
# 1.异常的追踪信息
# 2.异常的类型
# 3.异常的内容


# 为何处理异常？
# 为了增强程序的健壮性，即便是程序运行出错了，也不要终止程序
# 而是捕捉异常，将出错信息记录在日之内

# 逻辑上的错误
# 1.错误的发生是可以预知的，使用if判断来解决

# 2.错误的发生是无法预知的
"""
try:
    子代码块
except 异常类型1 as e1:
    pass
except 异常类型2 as e2:
    pass
else:
    如果没有异常发生，则会执行else的子代码
finally:
    无论被检测的代码是否有异常，都会执行finally的子代码

print("后续代码。。")
"""

print("start")
try:
    print("111111")
    l = ["aaa", "bbb"]
    # l[3] #抛出异常IndexError，该行代码不会继续运行
    print("22222")
    xxx
    print("333333")
    dic = {"a": 1}
    # dic["aaaa"]
# except (IndexError,NameError) as e:
#     print("异常被处理了",e)
# except KeyError as e1:
#     print("异常被处理了",e1)
except Exception as e2:
    print("所有异常都能匹配到", e2)
# else:
#     print("======>")
finally:  # 无论是否发生异常都会执行finally的子代码
    print("finally=====>应该把被检测代码块中回收系统资源的代码放到这里")

print("end")
