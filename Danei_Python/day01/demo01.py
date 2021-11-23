"""# 第一版
def get_prime(begin,end):
    list_result = []
    # 生成范围内的整数
    for number in range(begin,end):
        # 判断素数
        for item in range(2,number):
            if number % item ==0:
                break
        else:
            list_result.append(number)
    return list_result
"""


def is_prime(number):
    """
        判断是否是素数
    :param number: 指定的整数
    :return: Ture表示是素数，False表示不是素数
    """
    for item in range(2, number):
        if number % item == 0:
            return False
    return True


def get_prime(begin, end):
    """
        获取范围内的素数
    :param begin: 开始值（包含）
    :param end: 结束值（不包含）
    :return: 所有素数的列表
    """
    # 第二版
    # list_result = []
    # # 生成范围内的整数
    # for number in range(begin, end):
    #     if is_prime(number):
    #         list_result.append(number)
    # return list_result
    # 第三版
    return [number for number in range(begin, end) if is_prime(number)]


print(get_prime(5, 30))
