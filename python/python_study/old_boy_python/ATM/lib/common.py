"""
    存放配置信息
"""
import hashlib
import logging.config
from config import settings

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

# 添加日志功能(日志功能在接口层使用)
import logging
def get_logger(log_type):
    """
    :param log_type:比如是 user日志，bank日志，购物商城日志
    """
    #1.加载日志配置信息
    logging.config.dictConfig(
        settings.LOGGING_DIC
    )
    #2.获取日志对象
    logger = logging.getLogger(log_type)
    return logger