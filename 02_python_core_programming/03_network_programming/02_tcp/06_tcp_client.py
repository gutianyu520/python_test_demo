# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 13:20
# @Author  : Lim Yoona
# @Site    : 
# @File    : 06_tcp_client.py
# @Software: PyCharm

"""
    TCP客户端
"""

from socket import *
from threading import Thread


def sendCl(cli):
    while True:
        sendData = input("请输入：")
        if sendData == 'exit':
            cli.close()
            exit()
        cli.send(bytes(sendData, 'utf-8'))


def readCl(cli):
    while True:
        if cli:
            recvData = cli.recv(1024)
            print('接收数据：%s' % recvData)
        else:
            break


if __name__ == '__main__':
    tcpc = socket(AF_INET, SOCK_STREAM)
    serAdd = ('192.168.159.1', 7788)
    tcpc.connect(serAdd)
    t1 = Thread(target=sendCl, args=(tcpc,))
    t2 = Thread(target=readCl, args=(tcpc,))
    t1.start()
    t2.start()
