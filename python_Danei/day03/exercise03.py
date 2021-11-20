list01 = [43, 34, 35, 75, 7, 54, 32, 99, 12, 43]


def find_even():
    for item in list01:
        if item % 2 == 0:
            yield item

def find_10_num():
    for item in list01:
        if item > 10:
            yield item

def find_10_50_num():
    for item in list01:
        if 10 < item < 50:
            yield item
# for i in find_10_50_num():
#     print(i)
def condition(cond):
    for item in list01:
        if cond(item):
            yield item

def find01(item):
    return item % 2 == 0

def find02(item):
    return item > 10

def find03(item):
    return 10 < item < 50

re = condition(find01)
for i in re:
    print(i)