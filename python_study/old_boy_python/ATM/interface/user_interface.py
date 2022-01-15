"""
    逻辑接口层
        用户接口
"""
from db import db_hander
from lib import common


# 注册接口
def register_interface(username, password, balance=15000):
    # 接收到注册之后的结果，并打印
    # 2查看用户是否存在
    # 2.1调用数据处理曾中的select函数，会返回用户字典或者None
    user_dic = db_hander.select(username)
    if user_dic:
        return False, "用户已存在！"
    # 3若用户不存在，则保存注册数据
    # 3.1组织用户的数据字典信息
    password = common.get_pwd_md5(password)
    user_dic = {
        "username": username,
        "password": password,
        "balance": balance,
        # 用于记录用户流水的列表
        "flow": [],
        # 用于记录用户的购物车
        "shop_car": {},
        # locked 用于记录用户是否被冻结，False代表没有被冻结，True已被冻结
        "locked": False,
    }
    # 3.2 保存数据
    db_hander.save(user_dic)

    return True, f"{username}注册成功！"


# 登录接口
def login_interface(username, password):
    # 1.校验用户数据是否存在
    user_dic = db_hander.select(username)
    # 若有冻结用户，则需要判断是否被锁定
    if user_dic['locked']:
        return False, "当前用户已被锁定！"
    # 2.判断用户是否存在
    if user_dic:
        # 给用户输入的密码进行加密
        password = common.get_pwd_md5(password)
        # 3.校验密码是否一致
        if password == user_dic.get("password"):
            return True, f"{username}登陆成功"
        else:
            return False, "密码错误"
    else:
        return False, "用户不存在请重新输入"


# 查看余额接口
def check_bal_interface(username):
    user_dic = db_hander.select(username)
    return user_dic["balance"]
