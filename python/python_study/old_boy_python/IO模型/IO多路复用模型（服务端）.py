"""
IO多路复用模型
当监管的对象只有一个时， 其实IO多路复用还比不上阻塞IO
但是多路复用可以一次性监管很多个对象

监管机制是操作系统本身就有的，如果想要用该监管机制（select）
需要导入对应的select模块
总结：
监管机制有很多
select机制  windows  linux都有
poll机制  只有linux由  poll和select 都可以监管多个对象，但是poll更多
上述两种机制都不是很完美 当监管的对象特别多的时候，可能会出现特别大的延时相应
epoll机制  只在linux才有
他给每个监管对象多绑定一个回调机制
一旦有相应，回调机制立刻发起提醒
针对不同操作系统，考虑不同的检测机制，书写代码太繁琐
自动选择不同平台
selectors模块
"""
import socket
import select

server = socket.socket()
server.bind((("127.0.0.1", 8088)))
server.listen(5)
server.setblocking(False)
read_list = [server]

while True:
    r_list, w_list, x_list = select.select(read_list, [], [])
    # print(res)
    # ([<socket.socket fd=416, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8088)>], [], [])
    for i in r_list:
        """针对不同对象做不同处理"""
        if i is server:
            conn, addr = i.accept()
            # 也应该添加到带监管机制中
            read_list.append(conn)
        else:
            res = i.recv(1024)
            if len(res) == 0:
                i.close()
                # 将无效的监管对象 移除
                read_list.remove(i)
                continue
            print(res)
            i.send(b"heiheihei")
