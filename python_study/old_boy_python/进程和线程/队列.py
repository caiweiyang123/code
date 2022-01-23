from multiprocessing import Queue, Process

# # 创建一个队列
# q = Queue(5)# 括号内可以穿数字，标示可以生成的队列最大可以同时存放的数量
#
# # 往队列中存数据
# q.put(111)
# q.put(2222)
# q.put(3333)
# q.put(4444)
# q.put(5555)
# # q.put(66666)#当队列满了之后  如果还与数据程序就会堵塞
#
# """
# 存取数据 存是为了更好的取
# 千方百计地存，简单快捷的取
# 同在一个屋檐下
# 差距为何那么大
# """
#
# v1 = q.get()
# v2 = q.get()
# v3 = q.get()
# v4 = q.get()
# v5 = q.get()
# # v6 = q.get_nowait() #队列中没有数据了，也会原地堵塞
# try :
#     v6 = q.get(timeout=2) #队列中没有数据了，等待三秒会报错
#     print(v6)
# except Exception as e:
#     print("都没了！",e)
# print(v1,v2,v3,v4,v5)
"""
q.full()
q.empty()
q.get_nowait()
再多进程的情况下是不精确的
"""

"""
IPC机制研究思路
    1.主进程跟子进程借助于队列通信
    2.子进程跟子进程借助于队列通信
"""

def producer(q):
    q.put("我是23号技师，很高兴为您服务")


def consumer(q):
    print(q.get())


if __name__ == '__main__':
    q = Queue()
    p = Process(target=producer, args=(q,))
    p1 = Process(target=consumer, args=(q,))
    p.start()
    p1.start()
