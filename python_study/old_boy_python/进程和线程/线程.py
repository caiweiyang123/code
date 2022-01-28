"""
1.线程是什么？
    -进程表示的是资源单位，
    -线程表示执行单位
    将操作系统比喻大的工厂，进程是车间，线程是一条一条流水线
    每一个进程自带一个线程。
    总结：进程是资源单位（起一个进程，只是在内存中开辟一块独立空间）
        线程是执行单位（正真被cpu执行的是进程里面的线程，线程是指代码的执行过程，执行代码所要的资源都找进程要）
    进程和线程都是虚拟单位，只是为了我们更加方便地描述问题
2.线程为何要有？
开设进程
    -1申请内存空间， 耗资源
    -2拷贝代码。  耗资源
开线程
    -一个进程内可以开设多个线程，在一个进程内开设线程不需要再次开内存空间和拷贝代码
总结：开设线程的开销远比开设进程的开销
    同一个进程下的多个线程资源是共享的！！！

3.线程如何用？

"""
# from multiprocessing import Process
# from threading import Thread
# import time
#
#
# def task(name):
#     print("%s is running" % name)
#     time.sleep(1)
#     print("is over")
#
#
# if __name__ == '__main__':
#     # 开启线程不需要在main下执行代码，直接书写就可以
#     # 但是约定俗成写在main下main
#     t = Thread(target=task,args=("egon",))
#     t.start()
#     print("主")


from threading import Thread
import time


class MyThead(Thread):
    def __init__(self, name):
        """针对双下划线结尾的方法同意读成  双下init"""
        # 重写了父类的方法 又不知道有什么功能，就先调用父类的方法
        super().__init__()
        self.name = name

    def run(self):
        print("%s id running" % self.name)
        time.sleep(1)
        print("egon dsb")


if __name__ == '__main__':
    t = MyThead("egon")
    t.start()
    print("主")
