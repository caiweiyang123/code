"""
    什么是池？
    池是用来保证计算机硬件安全的情况下最大限度地利用计算机
    他降低了程序的运行效率但是保证了计算机硬件的安全，从而让你写的程序能够正常进行
"""
import os
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

# pool = ThreadPoolExecutor(5)  # 池子里就只有五个线程
# 括号内可以传数字 不穿默认是当前cpu的五倍的线程
pool = ProcessPoolExecutor()  # 括号内可以传数字 不穿默认是当前cpu的个数的的进程
"""
池子造出来之后，里面会固定存在五个线程
这五个线程不会出现重复创建和销毁的过程
池子造出来之后，里面会固定存在几个进程
这几个进程不会出现重复创建和销毁的过程

池子的使用很简单
只需要将需要做的任务往池子里提交即可，自动会有人来服务
"""


def task(n):
    print(n,os.getpid())
    time.sleep(2)
    return n ** 2

def call_back(n):
    print("call_bask",n.result())
"""
    任务的提交方式
        同步：提交任务后原地等待任务返回结果，期间不做任何事
        异步：提交任务后不等待任务的结果，继续执行
            返回结果怎么获取？
            异步提交任务的返回结果  应该通过回调机制来获取
            回调机制
                就相当于给每个异步任务绑定了一个定时炸弹
                一旦该任务有结果了就立刻触发爆炸
"""
if __name__ == '__main__':
    # pool.submit(task,1)  # 朝池子里提交任务  异步提交
    # print("主")
    t_list = []
    for i in range(20):  # 朝池子里提交了20个任务
        res = pool.submit(task, i).add_done_callback(call_back)
        # print(res.result())  # result 方法
        t_list.append(res)
    # pool.shutdown()  # 关闭线程池 ，等待线程池中任务执行完毕后再得到结果
    # for t in t_list:
    #     print(">>>:", t.result())

"""
程序由并发变成了串行
并且会返回结果
"""

"""
总结：导模块，生成池子
"""