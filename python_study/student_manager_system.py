class StusentMoodel:
    """
        学生信息模型
    """

    def __init__(self, name="", age=0, score=0, id=0):
        """
            创建学生对象
        :param name: 学生姓名 str
        :param age: 年龄 int
        :param score: 分数 int
        """
        self.name = name
        self.age = age
        self.score = score
        self.id = id

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 18 <= value <= 25:
            self.__age = value
        else:
            raise ValueError("输入的年龄太大了")

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if 0 <= value <= 100:
            self.__score = value
        else:
            raise ValueError("输入的成绩不对")


class StudentManagerController:
    """
        学生管理控制器
    """
    # 初始化学生id
    __init_id = 1000
    __count = 0

    def __init__(self):
        """
            生成学生列表
        """
        self.__stu_list = []

    @property
    def stu_list(self):
        """
            属性化学生列表
        :return: 学生列表
        """
        return self.__stu_list

    def add_student(self, stu_info):
        """
            添加新学生
        :param stu_info: 学生信息
        """
        stu_info.id = self.__generate_id()
        self.__stu_list.append(stu_info)
        StudentManagerController.__count += 1

    def __generate_id(self):
        """
            生成学生id
        :return: 学生id
        """
        StudentManagerController.__init_id += 1
        return StudentManagerController.__init_id

    def remove_student(self, id):
        """
            删除学生
        :param id: 根据id删除
        """
        for item in self.__stu_list:
            if item.id == id:
                self.__stu_list.remove(item)
                return True
            return False

    def update_stu_info(self, stu_info):
        """
            根据学生编号修改学生信息
        :param stu_info: 传进来想要修改的学生对象
        :return: 是否修改成功
        """
        for item in self.__stu_list:
            if item.id == stu_info.id:
                item.name = stu_info.name
                item.age = stu_info.age
                item.score = stu_info.score
                return True
            return False

    def order_score(self):
        """
            根据成绩进行升序排序
        """
        # self.__stu_list.sort(key=lambda x:x.score, reverse=False)
        for i in range(len(self.__stu_list) - 1):
            for j in range(len(self.__stu_list) - 1 - i):
                if self.__stu_list[j].score > self.__stu_list[j + 1].score:
                    self.__stu_list[j], self.__stu_list[j + 1] = self.__stu_list[j + 1], self.__stu_list[j]


class StudentManagerView:
    """
        学生管理视图
    """

    def __init__(self):
        """
            构造了一个学生控制器的实例对象，方便后面调用学生控制器里的方法
        """
        self.__manager = StudentManagerController()

    def __display_menu(self):
        """
            打印学生信息系统的菜单
        """
        print("1)添加学生")
        print("2)显示学生")
        print("3)删除学生")
        print("4)修改学生")
        print("5)按照成绩升序显示学生")

    def __select_menu(self):
        """
            学信息系统的菜单选择控制
        """
        item = input("请输入：")
        if item == "1":
            self.__input_student()
        elif item == "2":
            self.__output_students(self.__manager.stu_list)
        elif item == "3":
            self.__delete_student()
        elif item == "4":
            self.__modify_student()
        elif item == "5":
            self.__order_by_score()

    def main(self):
        """
            学生视图类的主函数，用来启动主界面
        """
        while True:
            self.__display_menu()
            self.__select_menu()

    def __input_student(self):
        """
            输入添加的学生信息，保存到学生管理器的学生列表中
        """
        name = input("请输入姓名：")
        age = int(input("请输入年龄："))
        score = int(input("请输入成绩："))
        stu = StusentMoodel(name, age, score)
        self.__manager.add_student(stu)

    def __output_students(self, list_output):
        """
            打印学生信息
        :param list_output:想要输出的学生列表
        """
        for item in list_output:
            print(f"{item.id},{item.name},{item.age},{item.score}")

    def __delete_student(self):
        """
            根据id删除学生
        :return: 是否删除成功
        """
        id = int(input("请输入编号："))
        for item in self.__manager.stu_list:
            if item.id == id:
                self.__manager.remove_student(item.id)
                return "删除成功"
            else:
                return "删除失败"

    def __modify_student(self):
        """
            根绝id修改学生信息
        :return: 是否修改成功
        """
        stu = StusentMoodel()
        stu.id = int(input("请输入需要修改的学生编号："))
        stu.name = input("请输入学生名称：")
        stu.age = int(input("请输入学生年龄："))
        stu.score = int(input("请输入学生成绩："))
        if self.__manager.update_stu_info(stu):
            print("修改成功")
        else:
            print("修改失败")

    def __order_by_score(self):
        self.__manager.order_score()
        self.__output_students(self.__manager.stu_list)


if __name__ == '__main__':
    view = StudentManagerView()
    view.main()
