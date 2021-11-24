# a = [1, 2, 3, 4]
# c = 'abcdef'
# print(a[::-1])
# print(c[::-1])
# print(list(reversed(a)))
# print(list(reversed(c)))
#
# print('{greet} from {language}.'.format( language='Python',greet="Hello world"))
# # print('%s from %s.' % ("Hello world", 'Python'))
# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello():
#     return "Hello world!"
#
#
# if __name__ == '__main__':
#     app.run()

# li = ['a', 'b', 'c', 'd', 'e']
# for i, e in enumerate(li):
#     print("index:", i, "element:", e)
import timeit
# 生成测试所需要的字符数组
strlist = ["it is a long value string will not keep in memory" for n in range(100000000)]
def join_test():
    return "".join(strlist) # 使用 join 方法连接 strlist 中的元素并返回字符串
def plus_test():
    result = ""
    for i, v in enumerate(strlist):
        result += v
    return result

if __name__ == "__main__":
    join_timer = timeit.Timer("join_test()", "from __main__ import join_test")
    print(join_timer.timeit(number=100))
    plus_timer = timeit.Timer("plus_test()", "from __main__ import plus_test")
    print(plus_timer.timeit(number=100))