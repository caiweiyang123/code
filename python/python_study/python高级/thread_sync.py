from threading import Lock

total = 0
lock = Lock()
# 在同一个线程里，一定要注意acquire的次数要和release的次数相等
def add():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total += 1
        lock.release()


def desc():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total -= 1
        lock.release()


import threading

thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print(total)

# 1.用锁会影响性能
# 2.锁会引起死锁
#死锁的情况A（a,b）
