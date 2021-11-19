class Player():
    def __init__(self, hp, atk=10):
        self.hp = hp
        self.atk = atk

    def attack(self, other):
        # 打的逻辑
        print("玩家攻击敌人")
        other.damage(self.atk)

    def damage(self, value):
        self.hp -= value
        print("玩家受伤")
        if self.hp <= 0:
            self.__death()

    def __death(self):
        print("玩家死亡")
        print("游戏结束")


class Enemy:
    def __init__(self, hp, atk):
        self.hp = hp
        self.atk = atk

    def damage(self, value):
        # 手上的逻辑
        print("敌人受伤")
        self.hp -= value
        if self.hp <= 0:
            self.__death()

    def __death(self):
        # 死亡的逻辑
        print("死亡")
        print("掉装备")
        print("加分")

    def attack(self, other):
        print("敌人攻击玩家")
        other.damage(self.atk)


e01 = Enemy(1000, 500)
p01 = Player(2000, 500)
p01.attack(e01)
e01.attack(p01)
p01.attack(e01)
