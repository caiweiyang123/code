"""
    用户视图层
"""
from interface import user_interface, bank_interface, shop_interface
from lib import common

# 全局变量，记录用户是否已登陆
login_user = None


# 1.注册功能
# 分层版
def register():
    while True:
        # 1.让用户输入用户名与密码进行校验
        username = input("请输入用户名：")
        password = input("请输入密码：")
        re_password = input("请输入密码：")
        # 小的逻辑处理，比如两次密码是否一致
        if password == re_password:
            # 调用接口层的注册接口，将用户名与密码交给接口层来进行处理
            flag, msg = user_interface.register_interface(username, password)
            # 根据flag判断用户是否注册成功
            if flag:
                print(msg)
                break
            else:
                print(msg)


# 2.登录功能
def login():
    # 登录视图
    while True:
        # 让用户输入用户名与密码
        username = input("请输入用户名：")
        password = input("请输入密码：")
        # 调登录接口，将数据传给接口
        flag, msg = user_interface.login_interface(username, password)
        if flag:
            print(msg)
            global login_user
            login_user = username
            break
        else:
            print(msg)


# 3.查看余额
@common.login_auth
def check_balance():
    # 直接调用查看余额接口，获取用户余额
    balance = user_interface.check_bal_interface(
        login_user
    )
    print(f"用户{login_user},余额为{balance}!")


# 4.提现功能
@common.login_auth
def withdraw():
    while True:
        # 1.用户输入提现金额
        input_money = input("请输入要提现金额：").strip()
        # 2.判断用户输入金额是否是数字
        if not input_money.isdigit():
            print("请输入数字！")
            continue
        input_money = int(input_money)
        flag, msg = bank_interface.withdraw_interface(login_user, input_money)
        if flag:
            print(msg)
        else:
            print(msg)


# 5.还款功能
@common.login_auth
def repay():
    """
        银行卡还款，无论是信用卡还是储蓄卡，是否能充值任意大小的金额
    """
    while True:
        # 1.让用户输入还款金额
        input_money = input("请输入还款金额：").strip()
        # 2.判断用户输入的是否是数字
        if not input_money.isdigit():
            print("请重新输入金额！")
            continue
        else:
            input_money = int(input_money)
        # 3.判断用户输入的金额是否大于0
        if input_money > 0:
            # 4.调用还款接口
            flag, msg = bank_interface.repay_interface(login_user, input_money)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print("输入的金额不能小于等于0")


# 6.转账功能
@common.login_auth
def transfer():
    """
        1.接受用户输入的转账目标用户
        2.接受用户输入的转账金额
    """
    while True:
        # 1.输入转账的金额
        to_user = input("请输入转账目标用户：").strip()
        money = input("请输入转账金额：").strip()
        # 2.判断用户输入的金额是否大于0或者是否是数字
        if not money.isdigit() and money <= 0:
            print("请输入正确金额：")
            continue
        money = int(money)
        if money > 0:
            # 3.调用转账接口
            flag, msg = bank_interface.transfer_interface(login_user, to_user, money)
            if flag:
                print(msg)
                break
            else:
                print(msg)


# 7.查看流水功能
@common.login_auth
def check_flow():
    # 直接查看流水接口
    flow_list = bank_interface.check_flow_interface(login_user)
    if flow_list:
        for flow in flow_list:
            print(flow)
    else:
        print("当前用户没有流水")


# 8.购物功能
@common.login_auth
def shopping():
    shop_list = [
        ["蟹黄包", 20],
        ["回锅肉", 22],
        ["山东水饺", 15],
        ["油泼面", 18],
        ["mac笔记本", 8888],
    ]
    # 初始化购物车
    shop_car = {}
    while True:
        # 商品的列表(从文件中读取商品)
        # 打印商品信息，让用户选择
        print("="*15+"欢迎来到无烟城"+"="*15)
        for index, shop in enumerate(shop_list):
            print(f"商品编号：{index},商品名称:{shop[0]},商品单价：{shop[1]}")
        print("=" * 11 + "实现每个人有房住的梦想" + "=" * 11)
        # 让用户选择商品
        choice = input("请输入商品编号(是否结账y or n)：").strip()
        if choice == "y":
            # 判断购物车是否为空
            if not shop_car:
                print("购物车是空的，不能添加，请重新输入！")
                continue
            flag, msg = shop_interface.pay_interface(login_user, shop_car)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        elif choice == "n":
            # 判断购物车是否为空
            if not shop_car:
                print("购物车是空的，不能添加，请重新输入！")
                continue
            # 调用添加购物车接口
            flag, msg = shop_interface.add_shop_car_interface(login_user, shop_car)
            if flag:
                print(msg)
                break
        if not choice.isdigit():
            print("输入的不是数字")
            continue
        choice = int(choice)
        if choice not in range(len(shop_list)):
            print("请输入正确的商品编号")
            continue

        # 获取商品信息
        shop_name, shop_price = shop_list[choice]
        # 加入购物车 --> 获取购物车
        # 判断用户选择的商品是否重复，重复数量加1
        if shop_name in shop_car:
            shop_car[shop_name][1] += 1
        else:
            shop_car[shop_name] = [shop_price, 1]
        print("当前购物车：",shop_car)


# 9.查看购物车
@common.login_auth
def check_shop_car():
    # 调用查看购物车接口
    shop_car = shop_interface.check_shop_car_interface(login_user)
    print(shop_car)




# 10.管理员功能
@common.login_auth
def admin():
    from core.admin import admin_run
    admin_run()


# 创建函数功能字典
func_dic = {
    "1": register,
    "2": login,
    "3": check_balance,
    "4": withdraw,
    "5": repay,
    "6": transfer,
    "7": check_flow,
    "8": shopping,
    "9": check_shop_car,
    "10": admin,
}


# 视图层主程序
def run():
    while True:
        print("""
        ===== ATM + 购物车 =====
            1.注册功能
            2.登录功能
            3.查看余额
            4.提现功能
            5.还款功能
            6.转账功能
            7.查看流水
            8.购物功能
            9.查看购物车
            10.管理员功能
        ========= end =========
        """)
        choice = input("请输入功能编号：").strip()
        if choice not in func_dic:
            print("请输入正确的功能编号：")
            continue
        func_dic.get(choice)()  # func_dic.get("1")() --> register()
