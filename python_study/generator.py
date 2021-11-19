# g = (x*3 for x in range(10))
#
# while True:
#     try:
#         e= next(g)
#         print(e)
#     except:
#         print("没有更多的元素了")
#         break

# def func():
#     n = 0
#     while True:
#         n += 1
#
#         yield n
# p = func()
# print(next(p))

# def feibolaqi(length):
#     a, b = 0, 1
#     n = 0
#
#     while n < length:
#         # print(b)
#         yield b
#         a, b = b, a + b
#         n += 1
#     else:
#         return "没有更多元素了！"
#
#
# g = feibolaqi(6)
#
# print(next(g))
# print(next(g))
# print(next(g))

# def gen():
#     i = 0
#     while i<5:
#         temp = yield i
#         print("temp",temp)
#         i += 1
#     return "没有更多的值了"
#
# g = gen()
# # print(next(g))
# # print(next(g))
# # print(next(g))
# print(g.send(None))
# n1 = g.send("呵呵")
# print(n1)
# n2=g.send("哈哈")
# print(n2)

# 进程 》线程》协程

def task1(n):
    for i in range(n):
        print(f"正在搬第{i}块砖！")
        yield None

def task2(n):
    for i in range(n):
        print(f"正在听第{i}首歌！")
        yield None

g1 = task1(5)
g2 = task2(5)

while True:
    try:
        g1.__next__()
        g2.__next__()
    except:
        pass

# 生成器应用点协程

