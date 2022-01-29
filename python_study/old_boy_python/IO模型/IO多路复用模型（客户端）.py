"""
IO多路复用模型
当监管的对象只有一个时， 其实IO多路复用还比不上阻塞IO
但是多路复用可以一次性监管很多个对象

监管机制是操作系统本身就有的，如果想要用该监管机制（select）
需要导入对应的select模块
"""
import socket

client = socket.socket()
client.connect(("127.0.0.1", 8088))

while True:
    client.send(b"hello world")
    data = client.recv(1024)
    print(data)
