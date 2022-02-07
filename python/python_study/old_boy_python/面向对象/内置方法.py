"""
    什么是内置方法？
    定义：在类的内部，以__开头__结尾的方法
    特点：会在某种情况下自动触发的方法

    2.为何要用内置方法？
    为了定制化我们的类or对象

    3.如何使用内置方法
    __str__
    __del__
"""
#__str__:打印对象时自动触发，然后将返回值（必须时字符串类型）当作本次打印的结果输出
# class People:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return "打印了%s%s"%(self.name,self.age)
#
# obj = People("张飞",19)

#__del__：在清理对象时触发，会先执行该方法
class People:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.x = "占据了操作系统资源"

    def __del__(self):
        print("run.....")

obj = People("张飞",19)

# del obj
print("========>")