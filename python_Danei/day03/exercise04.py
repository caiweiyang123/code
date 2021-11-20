from common.list_helper import *

list01 = [43, 34, 35, 75, 7, 54, 32, 99, 12, 43]


def find01(item):
    return item % 2 == 0


def find02(item):
    return item > 10


def find03(item):
    return 10 < item < 50


generate01 = Listhelper.find_all(list01, find01)
for item in generate01:
    print(item)
