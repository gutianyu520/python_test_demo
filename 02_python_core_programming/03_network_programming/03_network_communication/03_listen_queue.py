# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 16:22
# @Author  : Lim Yoona
# @Site    : 
# @File    : 03_listen_queue.py
# @Software: PyCharm

"""
    listen队列
"""

"""
    当客户端连接数到达服务器的设置数之后，新的客户端不会连接成功，而是等待服务器
"""

from socket import *
from time import sleep


# 服务器
def Server():
    tcpS = socket(AF_INET, SOCK_STREAM)
    addr = ('', 7788)
    tcpS.bind(addr)
    conNum = int(input("请输入最大连接数："))
    tcpS.listen(conNum)

    while True:
        cli, cli_addr = tcpS.accept()
        print(cli_addr)
        sleep(1)


# 客户端
def client():
    conM = int(input("请输入最大连接数："))
    for i in range(conM):
        cli = socket(AF_INET,SOCK_STREAM)
        cli.connect(('192.168.159.1',7788))
        print(i)


