"""
进程：资源单位
线程：执行单位
协程：这个概念是程序员自己意淫出来的，不存在
    单线程下实现并发
    程序员在代码层面上检测所有IO操作，一旦遇到IO，在代码级别切换
    这样给CPU感觉没有IO，一直在运行，从而提升运行效率

多道技术
    切换+保存状态
    CPU两种切换
        1.程序遇到IO
        2.程序长时间占用
TCP服务端
    accept
    recv

代码如何做到  切换+保存状态
保存状态
    保存上一次我执行的状态，下一次来接着上一次的操作继续往后执行

"""
from gevent import monkey

monkey.patch_all()
import time
from gevent import spawn


# gevent  模块无法检测常见的一些IO操作，在使用的时候需要导入猴子补丁

# def func1():
#     for i in range(10000000):
#         i+1
#
# def func2():
#     for i in range(10000000):
#         i+1
# start_time = time.time()
# func1()
# func2()
# print(time.time()-start_time)
#
# def func1():
#     while True:
#         1000000+1
#         yield
#
# def func2():
#     g = func1()
#     for i in range(10000000):
#         i +1
#         next(g)
# #
# start_time = time.time()
# func2()
# print(time.time()-start_time)

def heng():
    print("hengheng")
    time.sleep(3)
    print("hengheng")


def haha():
    print("hahha")
    time.sleep(3)
    print("hahha")


def heihei():
    print("heihei")
    time.sleep(5)
    print("heihei")


start_time = time.time()
g1 = spawn(heng)
g2 = spawn(haha)
g3 = spawn(heihei)
g1.join()
g2.join()
g3.join()

print(time.time() - start_time)
