class Student():
    def __init__(self, name, age, sex, score):
        self.name = name
        self.age = age
        self.sex = sex
        self.score = score

    def print_info(self):
        print(f"{self.name}是{self.sex}学生,今年{self.age}岁，成绩是{self.score}。")


list01 = [
    Student("赵敏", 28, "女", 90),
    Student("苏大强", 68, "男", 60),
    Student("明玉", 30, "女", 70),
    Student("无忌", 29, "男", 90),
    Student("张三丰", 130, "男", 97),
]

def find_name():
    for i in list01:
        # item=i
        if i.name == "苏大强":
            return i

# stu=find_name()
# print(stu.name,stu.score)
def fund_sex_nv():
    list02 = []
    for i in list01:
        if i.sex == "女":
            list02.append(i)
    return list02

# list03=fund_sex_nv()
# for i in list03:
#     print(i.name,i.sex)
def find_age_30():
    count = 0
    for i in list01:
        if i.age>30:
            count+=1
    return count

# print(find_age_30())
def score_to_zero():
    for i in list01:
        i.score = 0
    return list01

# result = score_to_zero()
# for i in result:
#     i.print_info()

def get_name():
    list04 = []
    for i in list01:
        list04.append(i.name)
    return list04

# re = get_name()
# for i in re:
#     print(i)

def get_max_age():
    max_stu = list01[0]
    for i in range(1,len(list01)):
        if max_stu.age < list01[i].age:
            max_stu = list01[i]
    return max_stu

re = get_max_age()
re.print_info()
