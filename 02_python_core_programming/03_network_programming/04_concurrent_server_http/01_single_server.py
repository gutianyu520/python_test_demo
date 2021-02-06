# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 16:54
# @Author  : Lim Yoona
# @Site    : 
# @File    : 01_single_server.py
# @Software: PyCharm

"""
    单进程服务器
"""
"""
    单进程的服务器，只能对一个客户端进行服务，当listen队列有空闲时，新的客户端就可以连接
"""


from socket import *

if __name__ == '__main__':
    sockSer = socket(AF_INET, SOCK_STREAM)
    # 重复使用绑定信息
    sockSer.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    localAddr = ('', 7788)
    sockSer.bind(localAddr)
    sockSer.listen(5)
    while True:
        print('----主进程---等待新客户端的到来----')
        clientSo, cliAddr = sockSer.accept()
        print('---主进程负责处理的数据：%s' % str(cliAddr))
        try:
            while True:
                recvData = str(clientSo.recv(1024), 'utf-8')
                if recvData != 'exit':
                    print('recv[%s]:%s' % (str(cliAddr), recvData))
                else:
                    print('[%s]客户端已经关闭' % str(cliAddr))
                    break
        finally:
            clientSo.close()
    sockSer.close()
