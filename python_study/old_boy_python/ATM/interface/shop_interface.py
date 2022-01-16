"""
    购物车接口
"""
from db import db_hander
from lib import common

shop_logger = common.get_logger('shop')

# 商城准备结算接口
def pay_interface(login_user, shop_car):
    # 1.计算消费总额
    # {”商品名称“:[]}
    cost = 0
    for price_number in shop_car.values():
        price, number = price_number
        cost += (price * number)

    # 2.导入银行接口
    from interface import bank_interface
    # 3.逻辑校验成功后，调用银行的支付接口支付
    flag = bank_interface.pay_interface(login_user, cost)
    if flag:
        return True, "支付成功，准备发货"
    else:
        return False, "支付失败，余额不足"


# 购物车添加接口
def add_shop_car_interface(login_user, shop_car):
    # 1.获取当前用户的购物车
    user_dic = db_hander.select(login_user)
    # 2.添加购物车
    # 2.1判断当前用户的购物车是否已经存在
    for shop_name, price_number in shop_car.items():
        number = price_number[1]
        if shop_name in user_dic['shop_car']:
            user_dic['shop_car'][shop_name][1] += number
        else:
            user_dic['shop_car'].update(
                {shop_name: price_number}
            )
    db_hander.save(user_dic)
    return True, "添加购物车成功！"

# 查看购物车接口
def check_shop_car_interface(username):
    user_dic = db_hander.select(username)
    return user_dic['shop_car']