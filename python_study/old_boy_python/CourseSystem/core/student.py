"""
    学生视图
"""
from conf import common
from interface import student_interface
from interface import common_interface

student_info = {
    "user": None
}


def register():
    while True:
        username = input("请输入用户名：").strip()
        password = input("请输入密码：").strip()
        re_password = input("请确认密码：").strip()

        if password == re_password:
            # 调用接口层管理员注册层
            flag, msg = student_interface.admin_register_interface(
                username, password)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print("两次输入的密码不一致！")


def login():
    while True:
        username = input("请输入用户名：").strip()
        password = input("请输入密码：").strip()
        # 1.调用管理员登录接口
        flag, msg = common_interface.login_interface(username, password, user_type="student")
        if flag:
            print(msg)
            # 记录当前状态
            student_info["user"] = username
            break
        else:
            print(msg)


@common.auth("student")
def choice_school():
    while True:
        # 1.调接口获取所有学校
        flag, school_list = common_interface.get_all_school_interface()
        if not flag:
            print(school_list)
            break
        for index, school_name in enumerate(school_list):
            print(f"编号：{index}  学校名：{school_name}")

        choice = input("请输入学校编号：").strip()
        if not choice.isdigit():
            print("请输入数字：")
            continue
        choice = int(choice)

        if choice not in range(len(school_list)):
            print("请输入正确的编号：")
            continue

        school_name = school_list[choice]
        # 开始调用学生选择学校接口
        flag, msg = student_interface.add_school_interface(
            school_name, student_info.get("user"))
        if flag:
            print(msg)
            break
        else:
            print(msg)
            break


@common.auth("student")
def choice_course():
    while True:
        # 获取学生当前学校的课程
        flag, course_list = student_interface.get_course_list_interface(
            student_info.get("user")
        )
        if not flag:
            print(course_list)
            break

        # 2.打印课程列表，并让学生选择课程
        for index, course_name in enumerate(course_list):
            print(f"编号：{index}  课程名：{course_name}")

        choice = input("请输入课程编号：").strip()
        if not choice.isdigit():
            print("请输入数字：")
            continue
        choice = int(choice)

        if choice not in range(len(course_list)):
            print("请输入正确的编号：")
            continue
        # 3.获取选择的课程名称
        course_name = course_list[choice]
        # 4.调用学生选择课程接口
        flag,msg = student_interface.add_course_interface(course_name,student_info.get("user"))
        if flag:
            print(msg)
            break
        else:
            print(msg)


@common.auth("student")
def check_score():
    #1.直接调用查看分数接口
    score_dict = student_interface.check_score_interface(
        student_info.get("user")
    )
    if not score_dict:
        print("没有选择课程！")
    print(score_dict)


func_dic = {
    "1": register,
    "2": login,
    "3": choice_school,
    "4": choice_course,
    "5": check_score,
}


def student_view():
    while True:
        print("""
        1.注册
        2.登录
        3.选择校区
        4.选择某个校区的课程
        5.查看分数
        """)
        choice = input("请输入功能编号：").strip()

        if choice == "q":
            break

        if choice not in func_dic:
            print("输入的选择功能编号有误，请重新输入！")
            continue
        func_dic.get(choice)()
