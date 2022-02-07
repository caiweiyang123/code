"""
阻塞IO
之前写的都是阻塞IO
没有借助其他模块，只用for循环监控
总结：
虽然非阻塞IO感觉很牛逼
但是该模型会占用cpu并且不干活，让cpu不同空转
实际应用中不会考虑非阻塞IO模型，但是每个技术都有存在的价值，实际应用或者是思想借鉴
"""
import socket

server = socket.socket()
server.bind(("127.0.0.1", 8888))
server.listen(5)
server.setblocking(False)
# 将所有的网络阻塞变为非阻塞
r_list = []
del_list = []
while True:
    try:
        conn, addr = server.accept()
        r_list.append(conn)
    except BlockingIOError as e:
        # print("做其他事")
        for conn in r_list:
            try:
                data = conn.recv(1024)
                if len(data) == 0:
                    conn.close()
                    # 将无用的conn从列表删除
                    del_list.append(conn)
                    continue
                conn.send(data.upper())
            except BlockingIOError as e:
                continue
            except ConnectionResetError:
                conn.close()
                del_list.append(conn)
        for conn in del_list:
            r_list.remove(conn)
        del_list.clear()
    # while True:
    #     try:
    #         data = conn.recv(1024)
    #         if len(data) == 0: break
    #         print(data)
    #         conn.send(data.upper())
    #     except Exception as e:
    #         break
    # conn.close()
