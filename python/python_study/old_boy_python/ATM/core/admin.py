from core import src
# 添加用户
from interface import admin_interface


def add_user():
    src.register()


# 修改用户额度
def change_balance():
    while True:
        # 1.输入修改额度
        change_user=input("请输入需要修改的用户名：").strip()
        # 2.调用接口修改额度
        money = input("请输入需要修改的额度：").strip()
        if not money.isdigit():
            print("请输入正确的额度")
            continue
        flag,msg = admin_interface.change_balance_interface(change_user,money)
        if flag:
            print(msg)
            break
        else:
            print(msg)

def lock_user():
    # 1.输入被锁定用户
    while True:
        lock_user = input("请输入需要冻结的用户名：").strip()
        flag,msg = admin_interface.lock_user_interface(lock_user)
        if flag:
            print(msg)
            break
        else:
            print(msg)



admin_func = {
    "1": add_user,
    "2": change_balance,
    "3": lock_user,
}
"""
    课后作业
"""
def admin_run():

    while True:
        print("""
            1.添加账户
            2.修改额度
            3.冻结账户
        """)
        choice = input("请输入管理员功能编号：").strip()
        if choice not in admin_func:
            print("请输入正确的功能编号：")
            continue
        admin_func.get(choice)()  # func_dic.get("1")() --> register()