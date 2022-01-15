"""
    存放配置信息
"""
import hashlib


# md5加密
def get_pwd_md5(password):
    md5_obj = hashlib.md5()
    md5_obj.update(password.encode("utf-8"))
    salt = "宝塔" + password + "镇河妖"
    md5_obj.update(salt.encode("utf-8"))
    result = md5_obj.hexdigest()
    return result


# 登录认证装饰器
def login_auth(func):
    from core import src
    def inner(*args, **kwargs):
        if src.login_user:
            res = func(*args, **kwargs)
            return res
        else:
            print("用户未登录，请先登录！")
            src.login()

    return inner

# 添加日志功能
import logging
def get_logger(log_type):
    """
    :param log_type:比如是 user日志，bank日志，购物商城日志
    """
