"""
    使用property封装变量
"""
class Wife:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        # self.set_age(age)
        # self.__weight = weight
        self.set_weight(weight)

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if 18 <= value <= 30:
            self.__age = value
            return self.__age
        else:
            raise ValueError("年纪太大了")

    age = property(get_age,set_age)

    def get_weight(self):
        return self.__weight

    def set_weight(self, value):
        if 90 <= value <= 100:
            self.__weight = value
            return self.__weight
        else:
            raise ValueError("体重不满足我的要求")

if __name__ == '__main__':
    w01 = Wife("茜茜公主",22,95)
    w01.age = 25
    print(w01.age)