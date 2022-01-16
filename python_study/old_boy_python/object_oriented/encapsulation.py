"""
    封装是面向对象三大特性中最核心的一个特性
    封装<-->整合
"""

"""
1.将封装的属性进行隐藏
    如何隐藏：在属性名前加__前缀，就会实现一个对外隐藏属性效果
    该属性隐藏要注意的问题：
        1.在类的外部无法直接访问双下划线开头的属性和方法，但是知道了类名还是可以访问
         所以说这种操作并没有严格限制外部访问，仅仅是一种语法上的变形
    例子1：
        class Foo:
            __x = 1
        
            def __fun1(self):
                print("from test")
                
        f1 = Foo()
        f1._Foo__fun1()
        print(Foo.__dict__)
        
        2.这种隐藏对外不对内
    例子2.    
        class Foo:
            __x = 1
        
            def __fun1(self):
                print("from test")
        
            def f2(self):
                print(self.__x)
                self.__fun1()
        
        f1 = Foo()
        f1.f2()
        
        3.这种变形操作只在检查类体语法的时候发生一次，之后定义的__开头的属性都不会变形
    例子3.
        class Foo:
            __x = 1
        
            def __fun1(self):
                print("from test")
        
            def f2(self):
                print(self.__x)
                self.__fun1()
        Foo.__y = 3
        print(Foo.__y)

    为何要隐藏？
        1.隐藏数据
            防止被人修改类的数据
        2.隐藏函数
        class People():
            def __init__(self,name):
                self.__name = name
        
            def get_name(self):
                return self.__name
        
            def set_name(self,value):
                # 可以做其他操作，比如判断值是否满足要求
                self.__name = value
                return self.__name
"""


# property是一个装饰器，是用来绑定给对象的方法伪装成一个数据属性
# 案例一
# class People:
#     def __init__(self, name, weight, height):
#         self.name = name
#         self.weight = weight
#         self.height = height
#
#     @property
#     def bmi(self):
#         return self.weight / (self.height ** 2)
#
#
# p1 = People("cai", 70, 1.85)
# p2 = People("lpp", 45, 1.6)
# print(p1.bmi)
# print(p2.bmi)

#案例二
class People:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        print(self.__name)
        return self.__name

    def set_name(self, value):
        # 可以做其他操作，比如判断值是否满足要求
        if type(value) is not str:
            print("输入str类型名字")
            return
        self.__name = value

p1 = People("cai")
p1.set_name("aaa")
p1.get_name()