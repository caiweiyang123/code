import socket
from threading import Thread

server = socket.socket()
server.bind(("127.0.0.1", 8080))
server.listen(5)


def communication(conn):
    while True:
        try:
            data = conn.recv(1024)
            if len(data) == 0: break
            conn.send(data.upper())
        except Exception as e:
            print(e)
            break


def server(ip, port):
    server = socket.socket()
    server.bind((ip, port))
    server.listen(5)
    while True:
        conn, addr = server.accept()
        # 开设多进程或者多线程处理客户端通信
        t = Thread(target=communication, args=(conn,))
        t.start()


if __name__ == '__main__':
    s = Thread(target=server, args=("127.0.0.1", 8080))
    s.start()
