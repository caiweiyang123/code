from threading import Thread,active_count,current_thread
import time
import os


# 数据共享
# money = 100
#
# def task():
#     global money
#     money = 666
#
#
# if __name__ == '__main__':
#     t = Thread(target=task)
#     t.start()
#     t.join()
#     print(money)

def task():
    # print("hello world", os.getpid())
    print("hello world", current_thread().name)
    time.sleep(2)


if __name__ == '__main__':
    t = Thread(target=task)
    t1 = Thread(target=task)
    t.start()
    t1.start()
    # t.join()
    # t1.join()
    # print("主", os.getpid())
    # print("主",current_thread().name)
    print("主",active_count())