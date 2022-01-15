"""
    数据处理层
        -专门用户处理数据的
"""
import json, os
from config import settings


# 查看数据
def select(username):
    # 1.接收接口层传过来的username用户名，拼接用户json文件路径
    user_path = os.path.join(settings.USER_DATA_PATH, f"{username}.json")
    # 2.校验用户json文件是否存在
    if os.path.exists(user_path):
        # 3. 打开数据，并返回给接口曾
        with open(user_path, "r", encoding="utf-8")as f:
            user_dic = json.load(f)
            return user_dic
    # 默认return None


# 保存数据(添加新数据或者更新数据)
def save(user_dic):
    # 1拼接用户的路径
    username = user_dic.get("username")
    user_path = os.path.join(settings.USER_DATA_PATH, f"{username}.json")
    # 2.保存数据
    with open(user_path, "w", encoding="utf-8")as f:
        json.dump(user_dic, f, ensure_ascii=False)
