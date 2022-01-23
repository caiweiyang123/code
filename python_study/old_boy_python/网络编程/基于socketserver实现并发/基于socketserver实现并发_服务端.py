"""
    服务端满足两个特点：
        1.一直对外提供服务
        2.并发的服务多个客户端
"""
from socket import *
import subprocess
import struct

server = socket(AF_INET, SOCK_STREAM)
server.bind(("127.0.0.1", 8081))
server.listen(2)

while True:
    conn, client_addr = server.accept()

    while True:
        try:
            msg= conn.recv(1024)
            if len(msg) == 0: break

            conn.send(msg.upper())
        except Exception:
            break

    conn.close()
