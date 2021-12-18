dict_commodity_info = {
    101: {"name": "屠龙刀", "price": 7000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "六脉神剑", "price": 7000},
    106: {"name": "乾坤大挪移", "price": 11000},
}
list_order = []


def select_menu():
    """
        选择菜单
    """
    while True:
        item = input("1建购买，2建结算")
        if item == "1":
            buying()
        elif item == "2":
            settlement()


def settlement():
    """
        结算
    """
    print_orders()
    total_price = calculate_total_price()
    paying(total_price)


def paying(total_price):
    """
        支付
    :param total_price:支付的价格
    """
    while True:
        mongey = float(input(f"总价{total_price}元，请输入金额："))
        if mongey >= total_price:
            print("购买成功，找回：%d元" % (mongey - total_price))
            list_order.clear()
            break
        else:
            print("金额不足")


def calculate_total_price():
    total_price = 0
    for order in list_order:
        commodity = dict_commodity_info[order["cid"]]
        print(f"商品：{commodity['name']},单价：{commodity['price']},数量：{order['count']}")
        total_price += commodity['price'] * order['count']
    return total_price


def print_orders():
    """
        打印订单
    """
    for order in list_order:
        commodity = dict_commodity_info[order["cid"]]
        print(f"商品：{commodity['name']},单价：{commodity['price']},数量：{order['count']}")


def buying():
    """
        购买
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
        获取商品订单
    :return: 商品编号
    """
    while True:
        cid = int(input("请输入商品编号："))
        if cid in dict_commodity_info:
            break
        else:
            print("该商品不存在")
    return cid


def print_commodity_info():
    for key, value in dict_commodity_info.items():
        print(f"编号：{key},名称：{value['name']},单价：{value['price']}")

select_menu()