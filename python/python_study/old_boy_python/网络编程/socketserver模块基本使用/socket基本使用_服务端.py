import socketserver


class MyRequestHandle(socketserver.BaseRequestHandler):
    def handle(self):
        # print(self.request)  # 如果tcp协议，self.request=>conn
        print(self.client_address)

        while True:
            try:
                msg = self.request.recv(1024)
                if len(msg) == 0: break

                self.request.send(msg.upper())
            except Exception:
                break

        self.request.close()


# 服务端应该做两件事
# 第一件事，循环地从半连接池中取出连接请求与其建立双向链接，拿到连接对象
s = socketserver.ThreadingTCPServer(("127.0.0.1", 8888), MyRequestHandle)
s.serve_forever()
# 等同于
# while True:
#     conn, client_addr = server.accept()
#     启动一个线程（conn，client_addr）
