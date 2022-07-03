"""
chat room
env:python3.6
socket udp & fork
"""
from socket import *
import os, sys

# 服务期地址
ADDR = ("0.0.0.0", 8882)

# 存储用户
user = {}


# 登录
def do_login(s, name, address):
    if name in user:
        s.sendto("该用户存在".encode(), address)
        return
    s.sendto(b"OK", address)

    # 通知其他人
    msg = "欢迎'%s'进入聊天室" % name
    for i in user:
        s.sendto(msg.encode(), user[i])
    user[name] = address  # 用户信息保存进字典

# 聊天
def do_chat(s,name,text):
    msg = "%s:%s"%(name,text)
    for i in user:
        # 排除本人
        if i !=name:
            s.sendto(msg.encode(),user[i])

def do_request(s):
    while True:
        data, addr = s.recvfrom(1024)
        tmp = data.decode().split(" ")  # 拆分请求
        # 根据不同的请求类型具体执行不同的事情
        # L 进入   C 聊天   Q 退出
        if tmp[0] == "L":
            do_login(s, tmp[1], addr)  # 执行具体工作
        elif tmp[0] == "C":
            text = " ".join(tmp[2:])
            do_chat(s,tmp[1],text)

# 搭建网络
def main():
    # udp 服务端
    s = socket(AF_INET, SOCK_DGRAM)
    # s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)

    # 请求处理函数
    do_request(s)


if __name__ == '__main__':
    main()
