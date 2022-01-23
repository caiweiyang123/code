# import os
# path = os.path.dirname(__file__)
# print(path)

# 什么是反射？
# 指的是在程序运行过程中可以”动态“获取对象的信息

# 为何要有反射？

# 如何实现反射？
class People
    def __init__(self, name, age)
        self.name = name
        self.age = age

    def say(self)
        print(f{self.name}今年{self.age}岁)


p1 = People(cai, 18)


# 实现反射机制的步骤
# 1.查看某一个对象下可以有哪些属性？
# print(dir(p1))
# print(dir(p1)[-2])
# 2.可以通过字符串反射到真正的属性上，得到属性值
# print(p1.__dict__[dir(p1)[-2]])

# 四个内置函数,通过字符串操作属性值
# hasattr()
# print(hasattr(p1, name))
# print(hasattr(p1, x))
# getattr()
# print(getattr(p1, name))
# setattr()
# print(setattr(p1, name, cwy))
# print(p1.name)
# delattr()
# delattr(p1, name)
# print(p1.__dict__)


# res = getattr(People,say)
# res1 = getattr(p1,say)
# print(res)
# print(res1)

class Ftp
    def put(self)
        print(正在上传)

    def get(self)
        print(正在下载)

    def interactive(self)
        method = input().strip()  # method=put

        if hasattr(self, method)
            getattr(self, method)()
        else
            print(输入指令不存在！)

obj = Ftp()
obj.interactive()