"""
    继承 -- 设计
"""

# 需求：老张开车去东北
# 变化：  坐火车，坐飞机，骑马

class Person:
    def __init__(self,name):
        self.name = name

    def go_to(self,vehicle,position):
        vehicle.transport(position)
        # if isinstance(vehicle,Car):
        #     vehicle.run(position)
        # elif isinstance(vehicle,Airplane):
        #     vehicle.flay(position)
class Vehicle():
    """
        交通工具，代表所有具体的交通工具（火车/飞机。。。）
    """
    def transport(self,position):
        pass
class Car(Vehicle):
    def transport(self,position):
        print("汽车开到",position)

class Airplane(Vehicle):
    def transport(self,position):
        print("飞机飞到",position)

p01 = Person("老张")
c01=Car()
a01 = Airplane()
p01.go_to(c01,"东北")
p01.go_to(a01,"东北")
