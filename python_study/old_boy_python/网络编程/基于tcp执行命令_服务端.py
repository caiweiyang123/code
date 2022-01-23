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
server.listen(5)

# 服务端应该做两件事
# 第一件事，循环地从半连接池中取出连接请求与其建立双向链接，拿到连接对象
while True:
    conn, client_addr = server.accept()

    # 第二件事，拿到连接对象，与其进行通信循环
    while True:
        try:
            cmd = conn.recv(1024)
            if len(cmd) == 0: break
            obj = subprocess.Popen(cmd.decode("utf-8"),
                                   shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout_res = obj.stdout.read()
            stderr_res = obj.stderr.read()
            total_size = len(stdout_res) + len(stderr_res)
            # 先发头信息（固定长度）：对数据描述信息
            header = struct.pack("i", total_size)
            conn.send(header)
            # 再发真实的数据
            conn.send(stdout_res + stderr_res)
        except Exception:
            break

    conn.close()
