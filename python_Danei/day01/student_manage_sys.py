class StudentModel:
    """
        学生模型
    """

    def __init__(self, name="", age=0, score=0, id=0):
        """
            创建学生对象
        :param name: 姓名：str类型
        :param age: 年龄：int类型
        :param score: 成绩：float类型
        :param id: 编号（该学生对象的唯一标识）
        """
        self.name = name
        self.age = age
        self.score = score
        self.id = id


class StudentManagerController:
    """
        学生管理控制器，负责业务逻辑处理
    """
    # 类变量 ，表示初始编号
    __init_id = 1000

    def __init__(self):
        # 创建学生列表
        self.__stu_list = []

    @property  # 属性化
    def stu_list(self):
        """
            学生列表
        :return: 存储学生对象的列表
        """
        return self.__stu_list

    def add_student(self, stu_info):
        """
            添加一个新学生
        :param stu_info:没有编号的学生信息
        """
        stu_info.id = self.__generate_id()

        self.stu_list.append(stu_info)

    def __generate_id(self):
        StudentManagerController.__init_id += 1
        return StudentManagerController.__init_id

    def remove_student(self, id):
        """
            按编号移除学生信息
        :param id: 按学生编号移除
        :return: 返回是否移除成功
        """
        for item in self.__stu_list:
            if item.id == id:
                self.__stu_list.remove(item)
                return True  # 移除成功
        return False  # 移除失败

    def update_student(self, stu_info):
        # 根据stu_info修改其他信息
        for item in self.__stu_list:
            if item.id == stu_info.id:
                item.name = stu_info.name
                item.age = stu_info.age
                item.score = stu_info.score
                return True
        return False

    def order_by_score(self):
        for i in range(len(self.__stu_list)-1):
            for j in range(0,len(self.__stu_list)-i-1):
                if self.__stu_list[j].score < self.__stu_list[j+1].score:
                    self.__stu_list[j],self.__stu_list[j+1] = self.__stu_list[j+1],self.__stu_list[j]



class StudentManagerView:
    """
        学生管理器视图
    """

    def __init__(self):
        self.__manager = StudentManagerController()

    def __display_menu(self):
        print("1)添加学生")
        print("2)显示学生")
        print("3)删除学生")
        print("4)修改学生")
        print("5)按照成绩升序显示学生")

    def __select_menu(self):
        item = input("请输入：")
        if item == "1":
            self.__input_student()
        elif item == "2":
            self.__output_student()
        elif item == "3":
            self.__delete_student()
        elif item == "4":
            self.__modify_student()
        elif item == "5":
            # self.__manager.order_by_score()
            self.__output_student_by_score()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __input_student(self):
        name = input("请输入学生名字")
        age = int(input("请输入学生年龄"))
        score = int(input("请输入学生成绩"))
        stu = StudentModel(name, age, score)
        self.__manager.add_student(stu)

    def __output_student(self):
        count = len(self.__manager.stu_list)
        if count == 0:
            print("现在还没有学生，赶紧添加学生吧")
        else:
            print(f"现在有{count}个学生,分别是")
        for item in self.__manager.stu_list:
            print(f"学生编号：{item.id},学生姓名是：{item.name},学生年纪是：{item.age},学生成绩是：{item.score}")

    def __delete_student(self):
        stu_id = int(input("请输入想要删除的学生编号："))
        if self.__manager.remove_student(stu_id):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_student(self):
        stu_id = int(input("请输入想要修改的学生编号："))
        name = input("请输入新的学生名字：")
        age = int(input("请输入新的学生年龄："))
        score = int(input("请输入新的学生成绩："))
        stu_info = StudentModel(name, age, score, stu_id)
        if self.__manager.update_student(stu_info):
            print("修改成功")
        else:
            print("修改失败")

    def __output_student_by_score(self):
        self.__manager.order_by_score()
        self.__output_student()

"""
manager = StudentManagerController()
s01 = StudentModel("张三", 15, 88)
manager.add_student(s01)
manager.add_student(StudentModel("李四", 15, 88))

for item in manager.stu_list:
    print(item.name, item.id)
"""

""""# 测试删除学生
manager = StudentManagerController()
manager.add_student(StudentModel("zs"))
manager.add_student(StudentModel("ls"))
manager.add_student(StudentModel("ww"))
manager.remove_student(1001)
for item in manager.stu_list:
    print(item.id, item.name)
"""

"""
# 测试修改功能
manager = StudentManagerController()
manager.add_student(StudentModel("zs"))
manager.add_student(StudentModel("ls"))
manager.add_student(StudentModel("ww"))
for item in manager.stu_list:
    print(item.name,item.age,item.score,item.id)
manager.update_student(StudentModel("张三",19,100,1001))
print("修改后")
for item in manager.stu_list:
    print(item.name,item.age,item.score,item.id)
"""

view = StudentManagerView()
view.main()
