"""
    模块
"""
# as 可以起个别名，防止冲突
# 导入方式1
# 本质：使用变量名module01关联模块地址
# import module01
#
# module01.fun01()
# my02 = module01.Myclass02()
# my02.fun02()

# 导入方式2
# 本质： 将指定的成员导入到当前模块的作用域中
# 注意：导入进来的成员不要和当前模块中成员冲突（名称相同）
# from module01 import fun01
# from module01 import Myclass02
#
# fun01()
# my02 = Myclass02()
# my02.fun02()

# 导入方式3
# 本质： 将指定的模块的所有成员导入到当前模块的作用域中
# 注意：导入进来的成员和其他模块成员冲突
# from module01 import *
#
# fun01()
# my02 = Myclass02()
# my02.fun02()
