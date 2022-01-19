"""
    用于存放类的
    学校类，学生类，课程类，讲师类，管理员类
"""
"""
    存放那些类?
"""
from db import db_hander


# 父类，让所有类继承save和select方法
class Base:
    @classmethod
    def select(cls, username):  # Admin,username
        # obj:可能是 对象 or None
        obj = db_hander.select_data(cls, username)
        return obj

    def save(self):
        # 让db_hander中的save_data帮我保存对象数据
        db_hander.save_data(self)


class Admin(Base):
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd

    @classmethod
    def select(cls, username):  # Admin,username
        # obj:可能是 对象 or None
        obj = db_hander.select_data(cls, username)
        return obj

    def save(self):
        # 让db_hander中的save_data帮我保存对象数据
        db_hander.save_data(self)

    def create_school(self, school_name, school_addr):
        # 该方法内部来调用学校类实例化对象，并保存
        school_obj = School(school_name, school_addr)
        school_obj.save()

    def create_course(self, school_obj, course_name):
        # 1.调用课程类，实例化课程
        course_obj = Course(course_name)
        course_obj.save()
        # 2.获取当前学校对象，并将课程加到课程列表中
        school_obj.course_list.append(course_name)
        # 3.更新学校信息
        school_obj.save()

    def create_teacher(self, teacher_name, teacher_pwd):
        # 1.调用老师类，实例化老师对象，并保存
        teacher_obj = Teacher(teacher_name, teacher_pwd)
        teacher_obj.save()


class School(Base):
    def __init__(self, name, addr):
        self.user = name
        self.addr = addr

        # 每所学校都有相应的课程列表
        self.course_list = []


class Student(Base):
    def __init__(self, username, password):
        self.user = username
        self.pwd = password

        # 每个学生只能有一个校区
        self.school = None
        # 一个学生可以有多门课程
        self.course_list = []
        self.score_dict = {}

    def add_school(self, school_name):
        self.school = school_name
        self.save()

    def add_course(self, course_name):
        self.course_list.append(course_name)
        self.score_dict[course_name] = 0
        self.save()
        # 学生选择的课程对象，添加学生
        course_obj = Course.select(course_name)
        course_obj.student_list.append(self.user)
        course_obj.save()


class Course(Base):
    def __init__(self, course_name):
        self.user = course_name
        self.student_list = []


class Teacher(Base):
    def __init__(self, teacher_name, teacher_pwd):
        self.user = teacher_name
        self.pwd = teacher_pwd
        self.course_list_from_tea = []

    def show_course(self):
        return self.course_list_from_tea

    def add_course(self, course_name):
        self.course_list_from_tea.append(course_name)
        self.save()

    def get_student(self, course_name):
        course_obj = Course.select(course_name)
        return course_obj.student_list

    def change_score(self,course_name,student_name,score):
        # 获取学生对象
        student_obj = Student.select(student_name)
        # 再给学生对象中的课程修改分数
        student_obj.score_dict[course_name]=score
        student_obj.save()
