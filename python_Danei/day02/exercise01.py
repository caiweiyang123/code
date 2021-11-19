"""
    定义父类
        动物类（行为：叫）
    定义子类
        狗（行为跑）
        鸟（行为飞）
"""


class Animal():
    def __init__(self, height, weight, color):
        self.height = height
        self.weight = weight
        self.color = color

    def sound(self):
        print("所有动物都会叫")


class Dog(Animal):
    def run(self):
        print("狗会快速奔跑")


class Brid(Animal):
    def fly(self):
        print("所有鸟都会飞")


a01 = Animal(10.21, 11, "blue")
d01 = Dog(30, 20, "yellow")
b01 = Brid(10, 5, "white")

# print(isinstance(a01,Animal))
# print(isinstance(a01,Dog))
# print(isinstance(d01,Animal))
# print(isinstance(d01,Dog))
# print(isinstance(d01,Brid))
# print(isinstance(b01,Brid))
# print(isinstance(b01,Dog))
# print(isinstance(b01,Animal))
# print(issubclass(Animal,Dog))
# print(issubclass(Animal,Brid))
# print(issubclass(Dog,Animal))
# print(issubclass(Dog,Brid))
# print(issubclass(Brid,Brid))
# print(issubclass(Brid,Dog))
# print(issubclass(Brid,Animal))