# 定义在控制台中打印二维列表的函数
from pprint import pprint

list01 = [
    [12, 24, 35, 56],
    [2, 54, 8, 45],
    [12, 23, 57, 8],
    [32, 54, 42, 15]
]


def print_double_list(target_list):
    for item in range(len(target_list)):
        for j in target_list[item]:
            print(j, end=" ")
        print()


# print_double_list(list01)

def set_num(list01):
    for c in range(1, len(list01)):
        for i in range(c, len(list01)):
            list01[i][c - 1], list01[c - 1][i] = list01[c - 1][i], list01[i][c - 1]


set_num(list01)
pprint(list01)
