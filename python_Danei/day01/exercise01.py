class Wife():
    count = 0

    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby
        Wife.count += 1

    def print_info(self):
        print(f"我老婆叫{self.name},今年{self.age}大了,爱好{self.hobby}。")

    @classmethod
    def get_wife_num(cls):
        print(f"现在创建了{cls.count}老婆对象。")


w1 = Wife("陆佩佩", 27, "看书")
w2 = Wife("陆佩佩1", 28, "看电视")
w3 = Wife("陆佩佩3", 26, "赚钱")
Wife.get_wife_num()