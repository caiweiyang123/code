"""
    2048游戏核心算法
"""
list_merge = [0, 2, 0, 2]


# 1.零元素移至末尾
def zero_to_end():
    for i in range(-1, -len(list_merge) - 1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)


# 2.将相同数合并字
def merge():
    """
        合并
    """
    # 先将中间的零元素移至末尾
    # 再合并相邻相同元素
    zero_to_end()
    for i in range(len(list_merge) - 1):
        if list_merge[i] == list_merge[i + 1]:
            # 将后一个累加前一个之上
            list_merge[i] += list_merge[i + 1]
            del list_merge[i + 1]
            list_merge.append(0)


# 3.地图向左移动
map = [
    [2, 0, 0, 2],
    [4, 4, 2, 2],
    [2, 4, 0, 4],
    [0, 0, 2, 2]
]


def move_left():
    for i in map:
        global list_merge
        list_merge = i
        merge()


# 4. 地图向右移动
def move_right():
    """
        向右移动
    """

    for i in map:
        global list_merge
        list_merge = i[::-1]
        merge()
        i[::-1] = list_merge


# 5. 地图向上移动，向下移动
def move_up():
    pass


def square_matrix_transpose(sqr_matrix):
    """
        方阵转置
    :param sqr_matrix:二维列表类型的方阵
    """
    pass
