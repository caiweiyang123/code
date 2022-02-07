"""
阻塞IO
之前写的都是阻塞IO
"""
import socket

client = socket.socket()
client.connect(("127.0.0.1",8888))

while True:
    client.send(b"hello world")
    data = client.recv(1024)
    print(data)
    