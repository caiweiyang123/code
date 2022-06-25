# 3.1对数值进行取整
# print(round(1.247,2))
# x = 1.2782
# print(format(x,"0.2f"))
# print("value is {:0.3f}".format(x))

# 3.2执行精确地小数计算
a = 4.2
b = 2.1
c = a + b
print(c)
print(c == 6.3)
from decimal import Decimal

a = Decimal("4.2")
b = Decimal("2.1")
c = a + b
print(c, type(c))
print((a + b) == Decimal("6.3"))
