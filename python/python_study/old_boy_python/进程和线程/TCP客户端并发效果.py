import socket
from threading import Thread
from multiprocessing import Process


client = socket.socket()
client.connect(("127.0.0.1",8080))
while True:
    client.send(b"hello word")
    data = client.recv(1024)
    print(data.decode("utf-8"))
