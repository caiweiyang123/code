"""
    程序的入口
"""
import sys,os
from core import src

# 添加解释器环境变量
sys.path.append(os.path.dirname(__file__))

# 开始执行项目函数
if __name__ == '__main__':
    src.run()