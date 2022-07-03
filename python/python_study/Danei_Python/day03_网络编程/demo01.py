"""
http请求相应测试
"""
from socket import *

s= socket()
s.bind(("127.0.0.1",8000))
s.listen(3)

c,addr = s.accept()
print("Connect from ",addr)
data = c.recv(4096) #打印http请求
print(data)

response = """HTTP/1.1 200 OK
Content-Type:text/html

<h1>hello world</h1>
"""
c.send(response.encode())
c.close()
s.close()
