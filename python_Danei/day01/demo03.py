"""
    静态方法的引入
"""
list01 = [
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"]
]


class Vector2:
    """
        二维向量
        可以表示位置和方向
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def left():
        return Vector2(0, -1)

    @staticmethod
    def right():
        return Vector2(0, 1)

    @staticmethod
    def up():
        return Vector2(-1, 0)

    @staticmethod
    def down():
        return Vector2(1, 0)


# pos01 = Vector2(1, 2)
# l01 = Vector2.left()
# pos01.x += l01.x
# pos01.y += l01.y
# print(pos01.x, pos01.y)

class DoubleListHelper:
    @staticmethod
    def get_elements(target, vect_pos, vect_dir, count):
        list_result = []
        for i in range(count):
            vect_pos.x += vect_dir.x
            vect_pos.y += vect_dir.y
            elements = target[vect_pos.x][vect_pos.y]
            list_result.append(elements)
        return list_result


# num = DoubleListHelper.get_elements(list01, Vector2(1, 0), Vector2.right(), 3)
# print(num)
# num2 = DoubleListHelper.get_elements(list01, Vector2(2, 3), Vector2.left(), 2)
# print(num2)

# 练习
# num3 = DoubleListHelper.get_elements(list01, Vector2(1, 3), Vector2.left(), 3)
# print(num3)
# num4 = DoubleListHelper.get_elements(list01, Vector2(2, 2), Vector2.up(), 2)
# print(num4)
# num5 = DoubleListHelper.get_elements(list01, Vector2(0, 3), Vector2.down(), 2)
# print(num5)

"""
    定义敌人类
    --数据：姓名，血量，基础攻击力，防御力
    --行为：打印个人信息
    
    创建敌人列表（至少四个元素）
    查找姓名是灭霸的敌人对象
    查找所有死亡的敌人
    计算所有敌人的平均攻击力
    删除防御力小于10的敌人
    将所有敌人的攻击力增加50
"""


class Enemy():
    def __init__(self, name, blood_volume, aggressivity, defensive_power):
        self.name = name
        self.blood_volume = blood_volume
        self.aggressivity = aggressivity
        self.defensive_power = defensive_power

    def print_info(self):
        print(f"我叫{self.name}，我的初始生命值是{self.blood_volume}，"
              f"我的初始攻击力是{self.aggressivity}，我的初始防御力是{self.defensive_power}。")


list_enemy = [
    Enemy("灭霸", 1000, 50, 10),
    Enemy("日本人", 0, 30, 8),
    Enemy("恐龙", 2000, 70, 20),
    Enemy("老虎", 0, 40, 9),
]

# 1.查找姓名是灭霸的敌人对象
def get_name():
    for i in list_enemy:
        if i.name == "灭霸":
            i.print_info()

# get_name()

# 2.查找所有死亡的敌人
def find_volume_zero():
    for i in list_enemy:
        if i.blood_volume == 0:
            print(f"{i.name}的血量为零，挂了！")

# find_volume_zero()

# 3.计算所有敌人的平均攻击力
def get_avg_aggressivity():
    count = 0
    sum = 0
    for i in list_enemy:
        sum+=i.aggressivity
        count+=1
    return sum/count

# print(get_avg_aggressivity())

# 4.删除防御力小于10的敌人
def delete_enemy():
    list03 = []
    for i in list_enemy[::-1]:
        if i.defensive_power <10:
            continue
        else:
            list03.append(i)
    return list03
# list02=delete_enemy()
# for i in list02:
#     i.print_info()

# 5. 将所有敌人的攻击力增加50
def power_up():
    for i in list_enemy:
        i.aggressivity+=50

# power_up()
# for i in list_enemy:
#     i.print_info()