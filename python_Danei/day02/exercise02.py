"""
    定义父类
        车（数据：品牌，速度）
    定义子类
        电动车（数据：电池容量，充电功率）
"""


class Car():
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed


class Electrocar(Car):
    def __init__(self, brand, speed, battery_capacity, charging_power):
        self.battery_capacity = battery_capacity
        self.charging_power = charging_power
        super().__init__(brand, speed)


c01 = Car("奔驰", 200)

e01 = Electrocar("特斯拉", 150, 100, 100)
