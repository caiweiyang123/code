# 互斥锁
# 多个进程操作同一份数据时，会出现数据错乱的问题
# 针对上述问题，解决方式是加锁处理，将并发变成串行，牺牲效率但是保证了数据的安全
import time
from multiprocessing import Process, Lock
import json
import random


# 查票
def search(i):
    with open("data", mode="r", encoding="utf-8")as f:
        dic = json.load(f)
    print("用户%s查票余额：%s" % (i, dic.get("ticket_num")))
    return dic
    # 字典取值不要用[]的形式，推荐使用get   你写的代码打死都不能报错！！！


# 买票
def buy(i):
    with open("data", mode="r", encoding="utf-8")as f:
        dic = json.load(f)
    time.sleep(random.randint(1, 3))
    # 判断当前是否有票
    if dic.get("ticket_num") > 0:
        # 修改数据库
        dic["ticket_num"] -= 1
        # 写入数据库
        with open("data", "w", encoding="utf-8")as f:
            json.dump(dic, f)
        print("用户%s买票成功" % i)
    else:
        print("用户%s买票失败" % i)


def run(i, mutex):
    search(i)
    # 给买票环节加锁处理，抢锁
    mutex.acquire()
    buy(i)
    mutex.release()


if __name__ == '__main__':
    # 在主进程中生成一把锁，让子进程抢，谁先抢到谁买票
    mutex = Lock()
    for i in range(1, 11):
        p = Process(target=run, args=(i, mutex))
        p.start()
