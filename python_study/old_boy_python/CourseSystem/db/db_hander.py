"""
    用于保存对象和获取对象
"""
import os
import pickle

from conf import settings


def save_data(obj):
    # 1. 获取对象的保存文件夹路径
    # 以类名当作文件夹的名字
    # obj.__class__:获取当前对象的名字，obj.__class__.__name__:获取类的名字
    class_name = obj.__class__.__name__
    user_dir_path = os.path.join(settings.DB_PATH, class_name)
    # 2.判断文件夹是都存在，不存在则创建文件夹
    if not os.path.exists(user_dir_path):
        os.mkdir(user_dir_path)
    # 3. 拼接当前用户的pickle文件路径，以用户作为文件名
    user_path = os.path.join(user_dir_path, obj.user)
    # 4. 打开文件，保存对象
    with open(user_path, "wb") as f:
        pickle.dump(obj, f)


def select_data(cls, username):
    class_name = cls.__name__
    user_dir_path = os.path.join(settings.DB_PATH, class_name)
    # 2.判断文件夹是都存在，不存在则创建文件夹
    if not os.path.exists(user_dir_path):
        os.mkdir(user_dir_path)
    # 3. 拼接当前用户的pickle文件路径，以用户作为文件名
    user_path = os.path.join(user_dir_path, username)
    # 4.判断文件是否存在，存在再打开并返回，不存在，则代表用户不存在
    if os.path.exists(user_path):
        # 4. 打开文件，获取对象
        with open(user_path, "rb") as f:
            obj = pickle.load(f)
            return obj
