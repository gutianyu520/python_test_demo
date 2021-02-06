# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 18:11
# @Author  : Lim Yoona
# @Site    : 
# @File    : 02_multiprocessing_server.py
# @Software: PyCharm

"""
    多进程服务器
"""

"""
    总结：
        每个客户端都创建一个进程，能够多个多个客户端服务
        太多数量则很消耗资源
"""
from socket import *
from multiprocessing import *
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
            cli = Process(target=dealWithClient, args=(clientSo, cliAddr))
            cli.start()

            clientSo.close()
    finally:
        soSer.close()


if __name__ == '__main__':
    main()
