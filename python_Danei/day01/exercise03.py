"""
    面向对象描述下列场景：
        小明在招商银行取钱
"""


class Person:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        self.__money = value


class Bank:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        self.__money = value

    def get_money(self, person, value):
        self.money -= value
        person.money += value
        print(f"{person.name}取了{value}钱")


xm = Person("小明", 10000)
zsyh = Bank("招商银行", 100000)
zsyh.get_money(xm, 10000)
