import socket

# 1.买手机
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.拨通服务端电话
phone.connect(("127.0.0.1", 8080))
# 3.通信
while True:
    msg=input("请输入要发的消息>>>:").strip()
    if len(msg)==0:continue
    phone.send(msg.encode("utf-8"))
    data = phone.recv(1024)
    print(data.decode("utf-8"))

# 4.关闭连接
phone.close()
