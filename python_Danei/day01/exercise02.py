class Enemy():
    def __init__(self, name, hp, atk, defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.__defense = defense

    @property  # 创建property对象，只负责拦截读取操作
    def atk(self):
        return self.__atk

    @atk.setter  # 只负责拦截写入操作
    def atk(self, value):
        if value > 10 and value < 50:
            self.__atk = value
        else:
            raise ValueError("值错了")

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        if value > 100 and value < 200:
            self.__hp = value
        else:
            raise ValueError("超过范围了")


e01 = Enemy("灭霸", 170, 40, 10)
e01.hp = 250
e01.atk = 30
print(e01.hp)
