from model import StudentModel
from bll import StudentManagerController

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