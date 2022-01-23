import struct
from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(("127.0.0.1", 8888))

while True:
    msg = input("请输入命令>>:").strip()
    if len(msg) == 0: continue
    client.send(msg.encode("utf-8"))

    res = client.recv(1024)
    print(res.decode("utf-8"))

client.close()