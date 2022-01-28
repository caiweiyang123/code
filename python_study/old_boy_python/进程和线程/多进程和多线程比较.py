# 计算密集型
# from multiprocessing import Process
# from threading import Thread
# import os, time
#
#
# def task():
#     res = 0
#     for i in range(1, 100000000):
#         res *= i
#
#
# if __name__ == '__main__':
#     l = []
#     print(os.cpu_count())
#     start_time = time.time()
#     for i in range(12):
#         p = Process(target=task)
#         p.start()
#         l.append(p)
#     for p in l:
#         p.join()
#     print(time.time() - start_time)

from multiprocessing import Process
from threading import Thread
import os, time

def task():
    time.sleep(2)


if __name__ == '__main__':
    l = []
    print(os.cpu_count())
    start_time = time.time()
    for i in range(400):
        p = Process(target=task)
        p.start()
        l.append(p)
    for p in l:
        p.join()
    print(time.time() - start_time)


"""
总结：
    多进程和多线程都有各自的优势
    并且我们后面在写项目时通常是
        多进程下开设多线程
        这样既可以利用多核也可以节省资源消耗
"""