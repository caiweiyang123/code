# 面条版
"""
def register():
    while True:
        # 1.让用户输入用户名与密码进行校验
        username = input("请输入用户名：")
        password = input("请输入密码：")
        re_password = input("请输入密码：")
        # 小的逻辑处理，比如两次密码是否一致
        if password == re_password:
            # 接收到注册之后的结果，并打印
            # 2查看用户是否存在
            # 2.1若不存在，则让用户
            user_path = os.path.join(settings.USER_DATA_PATH, f"{username}.json")
            if os.path.exists(user_path):
                print("用户已存在请重新输入：")
                continue
            # 3若用户不存在，则保存注册数据
            # 4若用户存在，则让用户重新输入
            # 4.1组织用户的数据字典信息
            user_dic = {
                "username": username,
                "password": password,
                "balance": 15000,
                # 用于记录用户流水的列表
                "flow": [],
                # 用于记录用户的购物车
                "shop_car": {},
                # locked 用于记录用户是否被冻结，False代表没有被冻结，True已被冻结
                "locked": False,
            }

            # 用户数据：tank。json 艾根。json  存不是目的，目的是为了方便取
            # 4.2 拼接用户json文件路径

            with open(user_path, "w", encoding="utf-8")as f:
                json.dump(user_dic, f, ensure_ascii=False)
"""