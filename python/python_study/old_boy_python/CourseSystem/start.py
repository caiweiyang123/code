"""
    启动文件入口
"""
import os, sys
from core import src

sys.path.append(
    os.path.dirname(__file__)
)

if __name__ == '__main__':
    src.run()
