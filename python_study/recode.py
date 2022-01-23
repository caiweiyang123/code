#!/usr/bin/python3
# -*- coding: utf-8 -*-

dict_commodity_info = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 10000},
    104: {"name": "九阳神功", "price": 10000},
    105: {"name": "降龙十八掌", "price": 10000},
    106: {"name": "乾坤大挪移", "price": 10000}
}

list_order = []


def select_menu():
    """
        选择菜单
    :return:
    """
    while True:
        item = input("1键购买，2键结算")
        if item == "1":
            buying()
        elif item == "2":
            settlement()


def settlement():
    """
        结算
    """
    print_orders()
    total_price = get_total_price()

    paying(total_price)


def paying(total_price):
    """
        支付过程
    :param total_price: 需要支付的价格
    :return:
    """
    while True:
        money = float(input("总价%d元，请输入金额：" % total_price))
        if money > total_price:
            print("购买成功，找回：%d元。" % (money - total_price))
            list_order.clear()
            break
        else:
            print("金额不足。")


def get_total_price():
    total_price = 0
    for order in list_order:
        commodity = dict_commodity_info[order["cid"]]

        total_price += commodity['price'] * order['count']
    return total_price


def print_orders():
    """
        打印订单
    :return:
    """
    for order in list_order:
        commodity = dict_commodity_info[order["cid"]]
        print(f"商品：{commodity['name']},单价：{commodity['price']},数量：{order['count']}.")


def buying():
    """
        购买
    :return:
    """
    print_commodity_info()

    create_order()

    print("添加到购物车")


def create_order():
    """
        创建订单
    """
    cid = input_commodity_id()
    count = int(input("请输入购买数量："))
    order = {"cid": cid, "count": count}
    list_order.append(order)


def input_commodity_id():
    """
        获取商品编号
    """
    while True:
        cid = int(input("请输入商品编号："))
        if cid in dict_commodity_info:
            break
        else:
            print("该商品不存在")
    return cid


def print_commodity_info():
    """
        打印商品信息
    """
    for key, value in dict_commodity_info.items():
        print(f"编号：{key}，名称：{value['name']}，单价：{value['price']}。")

if __name__ == '__main__':

    select_menu()
