"""
    继承 -- 变量
"""


class Person:
    def __init__(self, name):
        self.name = name


# class Student(Person):
#     """
#         子类没有构造函数，用父类的构造函数
#     """
#     pass
#
# s01 = Student("zs")
# print(s01.name)

class Student(Person):
    # 子类若具有构造函数，则必须先调用父类的构造函数
    def __init__(self, name, score):
        super().__init__(name)
        self.score = score

p01 = Person("张三")
print(p01.name)

s01 = Student("李四",100)
print(s01.name,s01.score)