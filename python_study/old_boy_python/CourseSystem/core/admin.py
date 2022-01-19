"""
    管理员视图
"""
from interface import admin_interface, common_interface
from conf import common

admin_info = {
    "user": None
}


def register():
    while True:
        username = input("请输入用户名：").strip()
        password = input("请输入密码：").strip()
        re_password = input("请确认密码：").strip()

        if password == re_password:
            # 调用接口层管理员注册层
            flag, msg = admin_interface.admin_register_interface(
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
        flag, msg = common_interface.login_interface(username, password,user_type="admin")
        if flag:
            print(msg)
            # 记录当前状态
            admin_info["user"] = username
            break
        else:
            print(msg)


@common.auth("admin")
def create_school():
    while True:
        school_name = input("请输入学校名称：").strip()
        school_addr = input("请输入学校地址：").strip()

        flag, msg = admin_interface.create_school_interface(
            school_name, school_addr, admin_info.get("user")
        )
        if flag:
            print(msg)
            break
        else:
            print(msg)


@common.auth("admin")
def create_course():
    while True:
        # 1.让管理员先选校学校
        # 1.1调用接口，获取所有学校名称并打印
        flag, school_list_or_msg = common_interface.get_all_school_interface()
        if not flag:
            print(school_list_or_msg)
            break
        for index, school_name in enumerate(school_list_or_msg):
            print(f"编号：{index}，学校名：{school_name}")
        choice = input("请输入学校编号：").strip()
        if not choice.isdigit():
            print("请输入数字：")
            continue
        choice = int(choice)

        if choice not in range(len(school_list_or_msg)):
            print("请输入正确的编号：")
            continue
        # 获取选择后的学校名字
        school_name = school_list_or_msg[choice]
        # 请输入需要创建的课程名称
        course_name = input("请输入需要创建的课程名称：").strip()
        # 3.调用创建课程接口，让管理员去创建课程
        flag, msg = admin_interface.create_course_interface(
            school_name, course_name, admin_info.get("user"))
        if flag:
            print(msg)
            break
        else:
            print(msg)


@common.auth("admin")
def create_teacher():
    while True:
        # 1.管理员输入需要创建的老师名字
        teacher_name = input("请输入老师名称：").strip()
        #2.调用接口创建老师
        flag,msg = admin_interface.create_teacher_interface(teacher_name,admin_info.get("user"))
        if flag:
            print(msg)
            break
        else:
            print(msg)
func_dic = {
    "1": register,
    "2": login,
    "3": create_school,
    "4": create_course,
    "5": create_teacher,
}


# 管理员视图函数
def admin_view():
    while True:
        print("""
            1.注册
            2.登录
            3.创建学校
            4.创建课程
            5.创建讲师
        """)
        choice = input("请输入功能编号：").strip()

        if choice == "q":
            break

        if choice not in func_dic:
            print("输入的选择功能编号有误，请重新输入！")
            continue
        func_dic.get(choice)()
