"""
    封装：
        数据角度：将多个变量封装到一个自定义类中。
                    符合人类的思考方式
                    可以将数据与对数据的操作封装到一起
        功能角度：对外提供必要的功能，隐藏实现的细节
                --私有化，将名称命名为以双下划线开头，
                    内部修改成员名称
                --属性：对实例变量的保护（拦截读写操作）
                --__slots__
        设计角度 ：
            分而治之：将大的需求分解为多个类，每个类负责一个职责
            变则疏之：遇到变化点单独封装一个类
            ---------------------------
            高内聚：一个类有且只有一个发生变化的原因
            低耦合：类与类的关系松散，低联系
"""


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_self(self):
        print(self.name, self.age)


#
# s01 = Student("张无忌", 19)
# s01.age = 35
# s01.print_self()


class Student02:
    def __init__(self, name, age):
        self.name = name
        self.set_age(age)

    def get_age(self):
        return self.__age

    def set_age(self, value):
        self.__age = value

    def print_self(self):
        print(self.name)


# s02 = Student02("张无忌", 19)
# # s02.age = 35
# s02.print_self()


class Student03:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __get_age(self):
        return self.__age

    def __set_age(self, value):
        self.__age = value

    age = property(__get_age,__set_age)

# s03 = Student03("张无忌", 19)
# s03.age = 29
# print(s03.age)

class Student04:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value


# s03 = Student03("张无忌", 19)
# s03.age = 29
# print(s03.age)


class Student05:
    def __init__(self, name, age):
        self.name = name



s05 = Student05("张无忌", 19)
s05.name = "灭霸"
print(s05.name)