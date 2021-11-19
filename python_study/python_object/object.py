# -*- coding:utf-8
import threading
from datetime import *
from time import sleep


def test():
    sleep(1)
    x=0
    while (x==0):
        print(datetime.now())


def thd():
    Threads = []
    for i in range(10):
        t = threading.Thread(target=test)
        Threads.append(t)
        # t.setDaemon(True)
    for t in Threads:
        t.start()


if __name__ == '__main__':
    thd()
    print("end")
