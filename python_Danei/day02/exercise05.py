class Enemy():
    def __init__(self, name, hp, atk, defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.__defense = defense

    def __str__(self):
        return "这是一个敌人类。"
