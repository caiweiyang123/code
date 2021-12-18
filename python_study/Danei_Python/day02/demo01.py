"""
    使用方法封装属性，输入读取和修改隐藏的属性
"""


class Wife:
    def __init__(self, name, age, weight):
        self.name = name
        # self.__age = age
        self.set_age(age)
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

    def get_weight(self):
        return self.__weight

    def set_weight(self, value):
        if 90 <= value <= 100:
            self.__weight = value
            return self.__weight
        else:
            raise ValueError("体重不满足我的要求")


if __name__ == '__main__':
    # 测试数据
    w01 = Wife("铁扇公主", 28, 98)
    # w01.set_age(22)
    print(w01.get_weight())
