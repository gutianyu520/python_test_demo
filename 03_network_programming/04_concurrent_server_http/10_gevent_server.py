# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 21:30
# @Author  : Lim Yoona
# @Site    : 
# @File    : 10_gevent_server.py
# @Software: PyCharm
import sys,time,gevent
"""
    gevent版-TCP服务器
"""
from gevent import socket,monkey
monkey.patch_all()

def handle_req(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            conn.close()
            break
        print('recv: ',data)
        conn.send(data)

def sever(port):
    s = socket.socket()
    s.bind(('',port))
    s.listen(5)
    while True:
        cli, addr = s.accept()
        gevent.spawn(handle_req,cli)

if __name__ == '__main__':
    sever(7788)





