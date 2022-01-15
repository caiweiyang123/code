"""
    银行接口
"""
from db import db_hander


# 提现接口(手续费5%)
def withdraw_interface(username, money):
    # 1.先获取用户字典
    user_dic = db_hander.select(username)
    # 先校验用户钱是否足够
    balance = int(user_dic.get("balance"))
    money2 = int(money) * 1.05
    if balance >= money2:

        # 2.修改字典中的金额
        balance -= money2
        user_dic['balance'] = balance
        # 3.记录流水
        flow = f"用户{username}，提现金额{money}成功，手续费为{money2 - money}"
        user_dic['flow'].append(flow)
        # 4.再保存数据
        db_hander.save(user_dic)
        return True, flow
    else:
        return False, "提现金额不足，请重新输入！"


# 还款接口
def repay_interface(username, money):
    """
        1.获取用户的金额
        2.给用户加上金额
    """
    # 获取用户数据字典
    user_dic = db_hander.select(username)
    # 直接做加钱动作
    user_dic["balance"] += money
    # 记录流水
    flow = f"用户{username}还款:{money}成功,当前额度为{user_dic['balance']}"
    user_dic['flow'].append(flow)
    # 调用数据处理层，将修改后的数据更新
    db_hander.save(user_dic)
    return True, flow


# 转账接口
def transfer_interface(login_user, to_user, money):
    """
        1.获取”当前用户“数据
        2.获取”转账目标“数据
        3.获取转账金额
    """
    # 1.获取”当前用户“数据
    login_user_dic = db_hander.select(login_user)
    # 2.获取”转账目标“数据
    to_user_dic = db_hander.select(to_user)
    # 3.判断目标用户是否存在
    if not to_user_dic:
        return False, f"用户{to_user}不存在"
    # 4.目标用户存在，则判断”当前用户的金额“是否足够
    if login_user_dic["balance"] >= money:
        # 5.若足够，则开始给目标用户加钱，当前用户减钱
        # 5.1给当前用户减钱
        login_user_dic['balance'] -= money
        # 5.2给目标用户加钱
        to_user_dic["balance"] += money
        # 5.3记录当前用户流水和目标用户流水
        # 当前用户流水
        login_user_flow = f"用户{login_user}给用户{to_user}转账{money}元成功！"
        login_user_dic['flow'].append(login_user_flow)
        # 目标用户流水
        to_user_flow = f"用户{to_user}收到用户{login_user}转账{money}元成功！"
        to_user_dic['flow'].append(to_user_flow)
        # 6.保存用户数据
        db_hander.save(login_user_dic)
        db_hander.save(to_user_dic)
        return True, login_user_flow
    return False, "当前用户金额不足！"


# 查看流水接口
def check_flow_interface(username):
    user_dic = db_hander.select(username)
    return user_dic['flow']


# 支付接口
def pay_interface(login_user, cost):
    user_dic = db_hander.select(login_user)
    # 判断用户金额是否足够
    if user_dic['balance'] >= cost:
        user_dic['balance'] -= cost
        flow = f"用户{login_user}消费花了{cost}元"
        user_dic['flow'].append(flow)
        db_hander.save(user_dic)
        return True
    return False
