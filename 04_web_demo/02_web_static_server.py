# -*- coding: utf-8 -*-
# @Time    : 2021/2/6 10:08
# @Author  : Lim Yoona
# @Site    : 
# @File    : 02_web_static_server.py
# @Software: PyCharm

"""
    Web静态服务器-2-显示需要的页面
"""

import socket
from multiprocessing import Process
import re

def handleClient(cliSo):
    global responseHeaders, responseBody
    recvData = str(cliSo.recv(2014), 'utf-8')
    reqLines = recvData.splitlines()
    for line in reqLines:
        print(line)

    method = reqLines[0]
    print(method)
    getFilename = re.match('[^/]+(/[^ ]*)', method).group(1)
    print('path is ===> %s', getFilename)

    if getFilename == '/':
        getFilename = docoumentRoot + '/index.html'
    else:
        getFilename = docoumentRoot + getFilename

    print('local path is ===> %s', getFilename)

    try:
        f = open(getFilename)
    except IOError:
        responseHeaders = 'HTTP/1.1 404 not found\r\n'
        responseHeaders += '\r\n'
        responseBody = '===file not in path'
    else:
        responseHeaders = 'HTTP/1.1 200 OK\r\n'
        responseHeaders += '\r\n'
        responseBody = f.read()
        f.close()
    finally:
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

docoumentRoot = './html'

if __name__ == '__main__':
    main()



