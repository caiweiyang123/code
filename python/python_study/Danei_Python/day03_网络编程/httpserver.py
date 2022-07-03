from socket import *

def request(connfd):
    # 获取请求将请求内容提取出来
    data = connfd.recv(4096)
    if not data:
        return
    request_line = data.decode().split("\n")[0]
    info = request_line.split(" ")[1]
    # 判断是/则返回index.html 不是则是返回404
    if info =="/":
        with open("index.html","rb")as f:
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response +="\r\n"
            response += f.read().decode()
    else:
        response = "HTTP/1.1 404 Not Found\r\n"
        response += "Content-Type:text/html\r\n"
        response += "\r\n"
        response += "<h1>sorry</h1>"
    connfd.send(response.encode())

sockfd = socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(("0.0.0.0",8000))
sockfd.listen(3)
while True:
    connfd,addr = sockfd.accept()
    request(connfd) # 处理客户端请求