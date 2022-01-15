"""
    配置信息
"""
# 获取项目根目录路径
import os.path

BASE_PATH=os.path.dirname(os.path.dirname(__file__))
# 获取user_data文件夹的路径
USER_DATA_PATH=os.path.join(BASE_PATH,"db","user_data")
