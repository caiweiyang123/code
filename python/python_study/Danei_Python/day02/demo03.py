class Wife:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        # self.set_age(age)
        self.weight = weight
        # self.set_weight(weight)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 18 <= value <= 30:
            self.__age = value
        else:
            raise ValueError("年纪太大了")

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if 90 <= value <= 100:
            self.__weight = value
        else:
            raise ValueError("体重不满足我的要求")

if __name__ == '__main__':
    w01 = Wife("茜茜公主",22,95)
    w01.age = 24
    print(w01.age)