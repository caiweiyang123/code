"""
重点：
    1.GIL不是python的特点而是CPython解释器的特点
    2.GIL是保证解释器级别的数据安全
    3.GIL会导致同一个进程下的多个线程无法同时执行既无法利用多核优势
    4.针对不同的数据还是需要加不同的锁处理
    5.解释型语言的通病
"""
from threading import Thread, Lock
import time

mutex = Lock()
money = 100


def task():
    global money
    # with mutex:
    #     tmp = money
    #     time.sleep(0.01)
    #     money = tmp - 1
    mutex.acquire()
    tmp = money
    time.sleep(0.01)
    money = tmp - 1
    mutex.release()


if __name__ == '__main__':
    t_list = []
    for i in range(100):
        t = Thread(target=task)
        t.start()
        t_list.append(t)

    for t in t_list:
        t.join()
    print(money)
