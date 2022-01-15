"""
    银行接口
"""
from db import db_hander

# 提现接口(手续费5%)
def withdraw_interface(username,money):
    # 1.先获取用户字典
    user_dic = db_hander.select(username)
    # 先校验用户钱是否足够
    balance = int(user_dic.get("balance"))
    money2 = int(money)*1.05
    if balance>=money2:

        # 2.修改字典中的金额
        balance -=money2
        user_dic['balance']= balance
        # 3.再保存数据
        db_hander.save(user_dic)
        return True,f"用户{username}，提现金额{money}成功，手续费为{money2-money}"
    else:
        return False,"提现金额不足，请重新输入！"