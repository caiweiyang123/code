"""
    服务端的特点
        1.能够一直提供服务
        2.能提供给并发服务
"""
import socket

# 1.买手机
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 流式协议=》tcp协议

# 2.绑定手机卡
server.bind(("127.0.0.1", 8081))

while True:
    data,client_addr = server.recvfrom(1024)
    server.sendto(data.upper(),client_addr)
    print(data)
    print(client_addr)



server.close()