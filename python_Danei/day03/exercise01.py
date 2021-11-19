import time


def life_days(year, month, day):
    """
        根据生日计算活了多少天
    :param year: 年
    :param month: 月
    :param day: 日
    :return: 活的天数
    """
    tuple_time = time.strptime("%d-%d-%d" % (year, month, day), "%Y-%m-%d")
    life_second = time.time() - time.mktime(tuple_time)
    return int(life_second / 60 / 60 // 24)


re = life_days(1993, 6, 12)
print(re)
