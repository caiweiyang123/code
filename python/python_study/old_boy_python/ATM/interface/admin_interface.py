from db import db_hander
from lib import common

admin_logger = common.get_logger('admin')

# 修改额度接口
def change_balance_interface(username, money):
    user_dic = db_hander.select(username)
    if user_dic:
        # 修改额度
        user_dic['balance'] = int(money)
        # 记录流水
        update_balance_flow = f"用户{username}额度修改成功"
        user_dic['flow'].append(update_balance_flow)
        # 保存修改后的用户数据
        db_hander.save(user_dic)
        admin_logger.info(update_balance_flow)
        return True, update_balance_flow
    return False, "修改的用户不存在"


# 冻结用户接口
def lock_user_interface(username):
    user_dic = db_hander.select(username)
    if user_dic:
        # 将用户locked值改为True
        user_dic['locked'] = True
        # 记录冻结账户流水
        lock_user_flow = f"用户{username}的账户冻结成功"
        user_dic['flow'].append(lock_user_flow)
        # 保存用户数据
        db_hander.save(user_dic)
        return True, lock_user_flow
    return False, "冻结用户不存在"
