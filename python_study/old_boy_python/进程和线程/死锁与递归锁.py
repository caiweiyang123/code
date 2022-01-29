"""
    死锁
    递归锁的特点
        1.可以被连续的acquire和release
        2.但是只能被第一个抢到这把锁执行上述操作
        3.它内部有一个计数器，每acquire一次计数器加一  每release一次计数器就减一
        4.只要计数器不为0，那么其他人都无法抢到该锁
    信号量
        如果将互斥锁比喻抢一个厕所，信号量就是抢多个厕所
"""
# from threading import Thread,Lock,RLock
# import time
#
# # mutexa  = Lock()
# # mutexb  = Lock()
# mutexa=mutexb = RLock()
# # 类只要加括号多次产生的是不同对象
# # 如果你想要实现多次加括号得到的是相同对象， 单例模式
#
# class MyThread(Thread):
#     def run(self):
#         self.func1()
#         self.func2()
#
#     def func1(self):
#         mutexa.acquire()
#         print("%s 抢到a锁"%self.name)
#         mutexb.acquire()
#         print("%s 抢到b锁" % self.name)
#         mutexa.release()
#         mutexb.release()
#
#     def func2(self):
#         mutexb.acquire()
#         print("%s 抢到b锁" % self.name)
#         time.sleep(2)
#         mutexa.acquire()
#         print("%s 抢到a锁" % self.name)
#         mutexa.release()
#         mutexb.release()
#
# if __name__ == '__main__':
#     for i in range(10):
#         t = MyThread()
#         t.start()

# # 信号量
# from threading import Thread, Semaphore
# import time
# import random
#
# """
# 利用random 模块实现打印随机验证码（搜狗的一道面试题）
# """
# sm = Semaphore(2)  # 括号内的数字，写多少就有几个坑位
#
#
# def task(name):
#     sm.acquire()
#     print("%s正在用厕所" % name)
#     time.sleep(random.randint(1,5))
#     sm.release()
#
#
# if __name__ == '__main__':
#     for i in range(10):
#         t = Thread(target=task, args=("步兵%s号" % i,))
#         t.start()

"""
    Event事件
    一些进程/线程需要等到其他进程/线程结束了才能运行
"""
# from threading import Thread, Event
# import time
#
# event = Event()  # 造了一个红绿灯
#
#
# def light():
#     print("红灯亮了\n")
#     time.sleep(3)
#     print("绿灯亮了\n")
#     # 告诉等红灯可以走了
#     event.set()
#
#
# def car(name):
#     print("%s车正在等红灯\n" % name)
#     event.wait()  # 等待别人给信号可以走了
#     print("%s 车加油门开走了\n" % name)
#
#
# if __name__ == '__main__':
#     t = Thread(target=light)
#     t.start()
#     for i in range(20):
#         t = Thread(target=car, args=("%s"%i,))
#         t.start()

"""
线程q
同一个进程下多个线程数据是共享的
为什么同一个进程下还会使用队列呢
因为队列是 管道+锁
    所以队列是为了数据安全
"""
import queue

# 我们现在使用的队列都是在本地测试使用的

# 1.队列q 先进先出

# q = queue.Queue(3)
# q.put(111)
# q.get()
# q.get_nowait()
# q.get(timeout=3)
# q.full()
# q.empty()

# 后进先出q
# q = queue.LifoQueue()  # last in first out
# q.put(1)
# q.put(2)
# q.put(3)
# print(q.get())  # 3

# 优先级q   可以给放入队列中的数据设置进出优先级
q = queue.PriorityQueue(4)
q.put((10, "111"))
q.put((100, "222"))
q.put((0, "333"))
q.put((-5, "444"))  # (-5, '444')
print(q.get())
# put 括号内放元组，第一个数字越小 优先级越高
