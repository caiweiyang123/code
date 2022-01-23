"""
    服务端的特点
        1.能够一直提供服务
        2.能提供给并发服务
"""
import socket

# 1.买手机
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 流式协议=》tcp协议

# 2.绑定手机卡
phone.bind(("127.0.0.1", 8080))

# 3.开机
phone.listen(5)  # 5指的是半连接池的大小
print("服务端启动完成，监听地址为%s%s" % ("127.0.0.1", 8080))
# 4.等待电话连接请求
# 加上连接循环
while True:
    conn, client_addr = phone.accept()

    # 5.接收消息
    while True:
        try:  # windows处理方式
            data = conn.recv(1024)
            if len(data) == 0:  # linux这种处理
                break
            print("客户端发来的消息：", data.decode("utf-8"))
            conn.send(data.upper())
        except Exception:
            break

    # 6.关闭电话链接conn(必选的回收资源的操作)
    conn.close()

# 7.关机
phone.close()
