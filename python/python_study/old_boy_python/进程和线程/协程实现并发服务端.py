import socket
from threading import Thread
from gevent import monkey

monkey.patch_all()
from gevent import spawn

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
        spawn(communication, conn)


if __name__ == '__main__':
    g1 = spawn(server, "127.0.0.1", 8080)
    g1.join()
