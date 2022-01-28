import socket
from threading import Thread
from multiprocessing import Process

"""
服务端
    1.要有固定的IP和端口
    2.服务是24小时不间断提供服务 
    3.能够支持并发
养成看源码的习惯
先拷贝，抄的多了就会了 
"""
server = socket.socket()  # 阔内不加参数默认是TCP协议
server.bind(("127.0.0.1", 8080))
server.listen(5)


# 将服务的代码封装成一个函数
def task(conn):
    while True:
        try:
            data = conn.recv(1024)
            if len(data) == 0: break
            print(data.decode("utf-8"))
            conn.send(data.upper())
        except Exception as e:
            print(e)
    conn.close()


# 链接循环
while True:
    conn, addr = server.accept()
    # 叫其他人来服务客户
    # t = Thread(target=task,args=(conn,))
    t = Process(target=task,args=(conn,))
    t.start()