import struct
from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(("127.0.0.1", 8081))

while True:
    msg = input("请输入命令>>:").strip()
    if len(msg) == 0: continue
    client.send(msg.encode("utf-8"))
    # 解决粘包问题思路
    # 1.先收固定长度的头：解析出数据的描述信息，拿到数据总大小
    header = client.recv(4)
    total_size = struct.unpack("i",header)[0]
    # 2.recv_size=0,循环接收，每接收一次，recv_size+=接受的长度
    # 3.直到recv——size=总大小

    recv_aise = 0
    recv_data = b""
    while recv_aise < total_size:
        recv_data = client.recv(1024)  # 本次接收，最大接收1024个Bytes
        recv_aise += len(recv_data)
        print(recv_data.decode("gbk"), end="")
    else:
        print("命令结束")

client.close()

# 粘包问题出现的原因
# 1.tcp是流式协议，数据像流水一样黏在一起，没有任何边界区分
# 2.收数据没收干净，有残留，就会跟下一次结果混淆在一起

# 解决的核心法门就是：每次收干净，无残留
