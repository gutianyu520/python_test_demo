# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 18:31
# @Author  : Lim Yoona
# @Site    : 
# @File    : 03_multithreading_server.py
# @Software: PyCharm


"""
    多线程服务器
"""

from socket import *
from threading import *
from time import sleep


def dealWithClient(cli, addr):
    while True:
        recvData = str(cli.recv(1024), 'utf-8')
        if len(recvData)>0:
            print('recv[%s]:%s' % (str(addr), recvData))
        else:
            print('---客户端关闭--')
            break
    cli.close()


def main():
    soSer = socket(AF_INET, SOCK_STREAM)
    soSer.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    localAddr = ('', 7788)
    soSer.bind(localAddr)
    soSer.listen(5)

    try:
        while True:
            print('----主进程---等待新客户端的到来----')
            clientSo, cliAddr = soSer.accept()
            print('---主进程负责处理的数据：%s' % str(cliAddr))
            cli = Thread(target=dealWithClient, args=(clientSo, cliAddr))
            cli.start()

            clientSo.close()
    finally:
        soSer.close()


if __name__ == '__main__':
    main()