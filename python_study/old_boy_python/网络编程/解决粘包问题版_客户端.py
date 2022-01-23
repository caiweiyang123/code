import json
import struct
from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(("127.0.0.1", 8082))

while True:
    msg = input("请输入命令>>:").strip()
    if len(msg) == 0: continue
    client.send(msg.encode("utf-8"))
    # 接收端
    # 1.先收4个字节，从中提取接下来要收的头的长度
    x = client.recv(4)
    header_len = struct.unpack("i",x)[0]
    # 2.接收头并解析
    json_str_bytes = client.recv(header_len)
    json_str = json_str_bytes.decode("utf-8")
    header_dic = json.loads(json_str)
    print(header_dic)
    total_size = header_dic["total_size"]

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
