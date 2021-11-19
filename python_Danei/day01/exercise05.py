"""
    封装：
        数据角度：将多个变量封装到一个自定义类中。
                    符合人类的思考方式
                    可以将数据与对数据的操作封装到一起
        功能角度：对外提供必要的功能，隐藏实现的细节
                --私有化，将名称命名为以双下划线开头，
                    内部修改成员名称
                --属性：对实例变量的保护（拦截读写操作）
                --__slots__
        设计角度 ：
            分而治之：将大的需求分解为多个类，每个类负责一个职责
            变则疏之：遇到变化点单独封装一个类
            ---------------------------
            高内聚：一个类有且只有一个发生变化的原因
            低耦合：类与类的关系松散，低联系
"""

class Person:
    def __init__(self,name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value

    def teach(self,who,kill):
        print(f"{self.name}教{who.name}{kill}")

    def work(self,money):
        print(f"{self.name}上班，挣了{money}块。")

zwj = Person("张无忌")
zm = Person("赵敏")
zwj.teach(zm,"九阳神功")
zm.teach(zwj,"化妆")
zwj.work(10000)
zm.work(6000)