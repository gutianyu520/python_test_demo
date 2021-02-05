# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 18:42
# @Author  : Lim Yoona
# @Site    : 
# @File    : server.py
# @Software: PyCharm

from socket import *
import time

g_sockList = []


def main():
    serSo = socket(AF_INET, SOCK_STREAM)
    serSo.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    localAddr = ('', 7788)
    serSo.bind(localAddr)
    serSo.listen(1000)
    # 设置非阻塞
    serSo.setblocking(False)

    while True:
        try:
            cli = serSo.accept()
        except Exception as result:
            pass
        else:
            print('一个新客户端来了：%s' % str(cli))
            cli[0].setblocking(False)
            g_sockList.append(cli)
        delList = []
        for cliSo, cliAddr in g_sockList:
            try:
                recvData = cliSo.recv(1024)
                if len(recvData) > 0:
                    print('recv[%s]:%s' % (str(cliAddr), recvData))
                else:
                    print('---客户端已关闭---')
                    cliSo.close()
                    delList.append((cliSo, cliAddr))
            except Exception as result:
                pass

        for delDe in delList:
            g_sockList.remove(delDe)


if __name__ == '__main__':
    main()
