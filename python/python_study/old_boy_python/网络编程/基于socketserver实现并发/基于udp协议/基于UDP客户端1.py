import socket

# 1.买手机
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2.拨通服务端电话
while True:
    msg = input("请输入要发的消息>>>:").strip()
    # if len(msg) == 0: continue
    client.sendto(msg.encode("utf-8"), ("127.0.0.1", 8088))
    data, server_addr = client.recvfrom(1024)
    print(data)
    print(server_addr)

# 4.关闭连接
client.close()
