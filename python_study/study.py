# def normalize(name):
#     name = str(name)
#     return name.title()
#
# # 测试:
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)
from functools import reduce


def prod(L):
    def ji(x,y):
        return x*y
    reduce(ji(),L)
