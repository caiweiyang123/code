"""
生产者：生产/制造东西的
消费者：消费/处理东西的
该模型除了以上述两个之外还学要一个媒介
生产者和消费者不是直接交互的，而是借助于媒介做交互
生产者（做包子的）+消息队列（媒介）+消费者（吃包子的）
"""
from multiprocessing import Process, Queue,JoinableQueue
import time
import random


def producer(name, food, q):
    for i in range(3):
        data = "%s生产了%s%s" % (name, food, i)
        # 模拟延迟
        time.sleep(random.randint(1, 3))
        print(data)
        # 将数据放入队列中
        q.put(data)


def consumer(name, q):
    # 生产者胃口很大，关盘行动
    while True:
        food = q.get()  # 没有数据就会卡住
        # if food is None:break
        time.sleep(random.randint(1, 3))
        print("%s吃了%s" % (name, food))
        q.task_done()# 告诉队列


if __name__ == '__main__':
    # q = Queue()
    q = JoinableQueue()
    p1 = Process(target=producer, args=("大厨egon", "包子", q))
    p2 = Process(target=producer, args=("tank", "油条", q))
    c1 = Process(target=consumer, args=("小马哥", q))
    c2 = Process(target=consumer, args=("发哥", q))

    p1.start()
    p2.start()
    # 将消费者设置为守护进程
    c1.daemon =True
    c2.daemon =True
    c1.start()
    c2.start()
    p1.join()
    p2.join()

    # q.put(None)#肯定在所有生产者生产的数据的末尾
    # q.put(None)
    q.join() # 等待队列中所有的数据被取完在执行后面代码
    """
    JoinableQueue 每当往队列中加一个数据时，内部会有一个计数器+1
    每当调用task_done的时候，计数器-1
    q.join()当计数器为0时才会运行    
    """
    # 只要q.join执行完毕，说明消费者已经处理完毕了，消费者没有必要存在了