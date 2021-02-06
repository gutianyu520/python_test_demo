# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 19:45
# @Author  : Lim Yoona
# @Site    : 
# @File    : 06_epoll_server.py
# @Software: PyCharm

"""
    epoll服务器（linux）
"""
import select

"""
    优点：
        1.没有最大并发连接数限制，打开文件描述符（FD）的上限远大于1024
        2.效率提升，只有活跃可用的FD才会调用callback函数
        
    说明：
        EPOLLIN(可读)
        EPOLLOUT(可写)
        EPOLLET(ET模式)
    
        epoll对文件描述符的操作有两种模式：LT和ET两种，LT是默认模式
        区别：
            LT模式：当epoll检测到描述符事件发生并将此事件通知应用程序，应用程序可以不立即处理该事件。下次调用epoll时，会再次响应应用程序并通知此事件。
            ET模式：当epoll检测到描述符事件发生并将此事件通知应用程序，应用程序必须立即处理该事件。如果不处理，下次调用epoll时，不会再次响应应用程序并通知此事件。
"""


import socket

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(('',7788))
s.listen(10)
epoll = select.epoll()

#epoll.register(s.fileno()),select.EPOLLIN | select.EPOLLET)


conns = {}
addrss = {}
while True:
    epoll_List = epoll.epoll()
    for fd,events in epoll_List:
        if fd == s.fileno():
            conn, addr = s.accept()
            print('有新的客户端到来：%s'%addr)
            conns[conn.fileno()] = conn
            addrss[conn.fileno()] = addr
            epoll.register(conn.fileno(),select.EPOLLIN | select.EPOLLET)
        elif events == select.EPOLLIN:
            recvData  = conns[fd].recv(1024)

            if len(recvData)>0:
                print('recv:%s'%str(recvData,'utf-8'))
            else:
                epoll.unregister(fd)
                conns[fd].close()
                print("%s--下线--"%str(addrss[fd]))













