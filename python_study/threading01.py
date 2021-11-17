# # from threading import Thread
# #
# # from time import sleep
# #
# #
# # def download(n):
# #     images = ["aaa.jpg", "bbb.jpg", "ccc.jpg"]
# #     for image in images:
# #         print(f"正在下载{image}\n" )
# #         sleep(n)
# #         print(f"下载{image}成功\n")
# #
# #
# # def listenMusic(m):
# #     musics = ["大城小爱", "心跳", "过火", "挪威的森林"]
# #     for music in musics:
# #         sleep(m)
# #         print(f"正在听{music}\n")
# #
# #
# # if __name__ == '__main__':
# #     # 线程对象
# #     t = Thread(target=download, name="aa", args=(1,))
# #     t.start()
# #
# #     t1 = Thread(target=listenMusic, name="aa", args=(1,))
# #     t1.start()
# #     # n = 1
# #     # while True:
# #     #     print(n)
# #     #     sleep(1.5)
# #     #     n += 1
# #
# import threading
#
# #
# # money = 1000
# #
# # def run1():
# #     global money
# #     for i in range(100):
# #         money -=1
# #
# #
# # def run2():
# #     global money
# #     for j in range(100):
# #         money -=1
# #
# # if __name__ == '__main__':
# #     t1 = threading.Thread(target=run1,name='aa')
# #     t1.start()
# #     t2 = threading.Thread(target=run2,name='bb')
# #     t2.start()
# #
# #     t1.join()
# #     t2.join()
# #     print(f"money{money}")
#
# n = 0
#
#
# def task1():
#     global n
#     for i in range(1000000):
#         n += 1
#     print(f"---->task1中的N的值是：{n}")
#
#
# def task2():
#     global n
#     for i in range(1000000):
#         n += 1
#     print(f"---->task2中的N的值是：{n}")
#
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=task1, name='aa')
#     t1.start()
#     t2 = threading.Thread(target=task2, name='bb')
#     t2.start()
#
#     t1.join()
#     t2.join()
#     print(f"money{n}")
