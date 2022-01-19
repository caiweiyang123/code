"""
    公共方法
"""


# 多用户登录认证装饰器
def auth(role):
    """
    :param role:角色-->管理员，学生，老师
    :return:
    """
    from core import admin, student, teacher
    # 登录认证装饰器
    def login_auth(func):
        def inner(*args, **kwargs):
            if role == "admin":
                if admin.admin_info["user"]:
                    res = func(*args, **kwargs)
                    return res
                else:
                    print("没有登录请先登录！")
                    admin.login()

            elif role == "student":
                if student.student_info["user"]:
                    res = func(*args, **kwargs)
                    return res
                else:
                    print("没有登录请先登录！")
                    student.login()

            elif role == "teacher":
                if teacher.teacher_info["user"]:
                    res = func(*args, **kwargs)
                    return res
                else:
                    teacher.login()
            else:
                print("没有登录请先登录！")
                print("当前用户没有权限")

        return inner

    return login_auth
