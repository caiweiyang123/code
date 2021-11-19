"""
    异常处理
"""
def div_apple(apple_count):
    person_count = int(input("请输入人数："))
    result = apple_count/person_count
    print("每个人%d个苹果"%result)

try:
    div_apple(10)
except ValueError:
    print("输入的是整数")
except ZeroDivisionError:
    print("人数不能为0")
except Exception:
    print("未知的错误")


print("后续逻辑")