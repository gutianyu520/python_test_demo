# -*- coding: utf-8 -*-
# @Time    : 2021/2/6 9:50
# @Author  : Lim Yoona
# @Site    : 
# @File    : 01_web_static_server.py
# @Software: PyCharm

"""
    Web静态服务器-1-显示固定的页面
"""
import socket
from multiprocessing import Process


def handleClient(cliSo):
    # 客户端服务
    recvData = cliSo.recv(2014)
    requestHeaders = recvData.splitlines()
    for line in requestHeaders:
        print(str(line, 'utf-8'))

    responseHeaders = 'HTTP/1.1 200 OK\r\n'
    responseHeaders += '\r\n'
    responseBody = 'hello world'

    response = responseHeaders + responseBody
    cliSo.send(bytes(response, 'utf-8'))
    cliSo.close()


def main():
    # 主程序
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('', 7788))
    server.listen(10)
    while True:
        client, addr = server.accept()
        clientP = Process(target=handleClient, args=(client,))
        clientP.start()
        client.close()


if __name__ == '__main__':
    main()
