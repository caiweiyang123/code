"""
    一切皆为对象
    什么是元类？
    元类是用来实列化产生的类
    关系：元类-->实列化-->类（People）-->实列化-->对象（obj）
"""

# class People:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def say(self):
#         print("%s%s" % (self.name, self.age))


# obj = People("小菜", 22)
# print(People.__dict__)

# print(type(People))
# print(type(int))

# class 关键字创造类People的步骤
# 类有三大特征：
# 1.类名
class_name = "People"
# 2.类的基类
class_base = (object,)
# 3.执行类体代码，拿到类的名称空间
class_dict = {}
class_body = """
def __init__(self,name,age):
    self.name = name
    self.age = age

def say(self):
    print("%s%s"%(self.name,self.age))
        """


# exec(class_body, {}, class_dict)
# print(class_dict)

# 调用元类
# People = type(class_name, class_base, class_dict)
# obj1 = People("张三", 12)
# print(obj1.__dict__)
# obj1.say()


# People = Mymeta(class_name, class_base, class_dict)

# 何如自定义元类来控制类的产生？
# class Mymeta(type):
#     def __init__(self, x, y, z):
#         # if not x.istitle():
#         #     raise NameError("类名首字母必须大写")
#         print("run....")
#         # print(self)
#         # print(x)
#         # print(y)
#         # print(z)
#
#     #        当前所在的类，调用类时所传入的参数
#     def __new__(cls, *args, **kwargs):
#         print("1111111111111")
#         # print(cls)
#         # print(args)
#         # print(kwargs)
#         # return super().__new__(cls, *args, **kwargs)
#         return type.__new__(cls, *args, **kwargs)


# 调用Mymeta发生三件事
# 1.先造一个空对象，People,调用类里的__new__方法
# 2.调用Mymeta的__init__方法，完成初始化对象的操作
# 返回初始化好的对象
#
# class People(metaclass=Mymeta):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def say(self):
#         print("%s%s" % (self.name, self.age))


# 强调
# 只要是调用类，那么会依次调用
# 1.类内的__new__
# 2.类内的__init__


# __call__
class Foo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self, *args, **kwargs):
        print("111111111")


obj = Foo(11, 22)
obj()
# 应用：如果想让对象可以被调用，再该对象的类中加一个方法__call__
# 总结：
# 对象（）-->类内的__call__
# 类（）->自定义元类内的__call__
# 自定义元类（）->内置元类__call__

# 六：自定义元类控制类的调用=》类的对象的产生
class Mymeta(type):
    def __init__(self, x, y, z):
        print("run....")

    def __new__(cls, *args, **kwargs):
        print("1111111111111")

        return type.__new__(cls, *args, **kwargs)

# 类的产生
#
class People(metaclass=Mymeta):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print("%s%s" % (self.name, self.age))

# 属性查找的原则：对象——》类——》父类
# 父类不是元类
