# from multiprocessing import Process
# from time import sleep
#
# def task1():
#     while True:
#         sleep(1)
#         print("这是任务1。。。")
#
#
# def task2():
#     while True:
#         sleep(2)
#         print("这是任务2.。。。")
#
#
# if __name__ == '__main__':
#     # 子进程
#     p1 = Process(target=task1,name="任务一")
#     p1.start()
#     print(p1.name)
#     p2 = Process(target=task2,name="任务二")
#     p2.start()
#     print(p2.name)
#
#     print("---------")
#
#     # task1()
#     # task2()


# 进程通信
from multiprocessing import Process, Queue
from time import sleep


def download(q):
    images = ["aaa.jpg", "bbb.jpg", "ccc.jpg"]
    for image in images:
        print("正在下载。。。", image)
        sleep(0.5)
        q.put(image)


def getfile(q):
    while True:
        try:
            file = q.get(timeout=3)
            print(f"{file}文件保存成功")
        except:
            print("全部保存完毕！")
            break


if __name__ == '__main__':
    q = Queue(5)
    p1 = Process(target=download, args=(q,))
    p2 = Process(target=getfile, args=(q,))

    p1.start()
    p1.join()
    p2.start()
    p2.join()
    print("00000000000")