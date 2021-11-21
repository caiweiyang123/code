# 练习，累加一个四位数整数的每位和
def each_unit_sum(number):
    """
        累加一个四位数整数的每位和
    :param number: 四位数整数
    :return: 相加结果
    """
    result = number % 10
    result += number // 10 % 10
    result += number // 100 % 10
    result += number // 1000
    return result


# 测试代码
if __name__ == '__main__':
    re = each_unit_sum(1547)
    print(re)
