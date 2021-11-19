"""
    定义函数：从控制台获取成绩
    要求：如果异常，继续获取成绩，知道获取正确的成绩为止
        成绩必须要0到100之间
"""


def get_score():
    while True:
        try:
            score = int(input("请输入成绩："))
        except Exception:
            print("输入有误，请重新输入：")
        if 0 <= score <= 100:
            print("输入成绩正确")
            return score
        else:
            print("成绩不在范围内")


result = get_score()
print(result)
