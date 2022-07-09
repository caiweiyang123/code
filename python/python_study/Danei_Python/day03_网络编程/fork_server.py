"""
fork_server.py 基于fork的多进程并发
重点代码

1.创建监听套接字
2.等待接受客户端请求
3.客户端连接创建新的进程处理客户端请求
4.原进程继续等待其他客户端连接
5.如果客户端退出，则销毁对应的进程
"""
from socket import *
import os
import signal

#全局变量
HOST = "0.0.0.0"
PORT = 8888
ADDR=(HOST,PORT)

# 创建套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)

# 处理僵尸进程
signal.signal(signal.SIGCHLD,signal.SIG_IGN)
print("Listen the port 8888...")

while True:
    try:
        c,addr = s.accept()
        print("connect from",addr)
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue

    # 创建新的进程处理客户端事务
    pid = os.fork()
    if pid == 0:
        s.close()
        handle()# 处理具体事务
        os._exit(0) # 子进程销毁
    # 无论是父进程还是fork出错都要回去继续处理连接
    else:
        c.close()# 父进程不需要和客户端通信
