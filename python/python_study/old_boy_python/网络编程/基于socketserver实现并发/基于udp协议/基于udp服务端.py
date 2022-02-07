"""
    服务端的特点
        1.能够一直提供服务
        2.能提供给并发服务
"""
import socketserver

class MyRequestHandle(socketserver.BaseRequestHandler):
    def handle(self):
        client_data = self.request[0]
        server = self.request[1]
        client_address = self.client_address
        print("客户端发来的数据%s"%client_data)
        server.sendto(client_data,client_address)


s1 = socketserver.ThreadingUDPServer(("127.0.0.1", 8088), MyRequestHandle)
s1.serve_forever()
