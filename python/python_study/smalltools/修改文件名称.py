#!/usr/bin/python
# -*- coding:utf-8 -*-
import os.path

# 1.获取当前路径
folder_name = "/test_video"
path = os.path.dirname(__file__) + folder_name  # "E:\pyproject\test_video/"


# 修改目标目录里的文件名称
def refilename(path):
    """
    修改文件的名字为”xxx.mp4“
    :param path: 要修改的文件的路径
    :return: 没有返回值
    """
    filelist = os.listdir(path)
    n = 0
    for file in filelist:
        oldpathname = path + "/" + file
        filename = oldpathname.split("/")[-2]

        if os.path.isdir(oldpathname):
            refilename(oldpathname)  # "E:\pyproject\test_video/大件行李/"
        else:
            # 2.重命名文件
            newpathname = path + "/" + filename + str(n) + ".mp4"
            os.renames(oldpathname, newpathname)
        n += 1


if __name__ == '__main__':
    refilename(path)
