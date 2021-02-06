# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 13:07
# @Author  : Lim Yoona
# @Site    : 
# @File    : 05_tcp_server.py
# @Software: PyCharm
"""
    TCP服务器
"""
"""
    tcp服务器流程：
        1.socket():创建套接字
        2.bind(ip,port)：绑定ip和port
        3.listen()：是套接字变被动接收
        4.accept()：等待客户端连接
        5.rev/send：接收发送数据
"""
from socket import *

tcps = socket(AF_INET,SOCK_STREAM)
addr = ('',7788)
tcps.bind(addr)
tcps.listen(5)
newso,cliAr = tcps.accept()
recvData = newso.recv(1024)
print('接收到的数据：%s'%recvData)
newso.send(bytes('thanks!','utf-8'))
newso.close()
tcps.close()







