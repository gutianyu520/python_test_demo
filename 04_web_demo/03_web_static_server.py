# -*- coding: utf-8 -*-
# @Time    : 2021/2/6 10:29
# @Author  : Lim Yoona
# @Site    : 
# @File    : 03_web_static_server.py
# @Software: PyCharm

"""
    Web静态服务器-3-使用类
"""
import socket,sys,re
from multiprocessing import Process

class WSGIServer:
    addrFamily = socket.AF_INET
    addrType = socket.SOCK_STREAM
    listenLine = 5

    def __init__(self,address):
        self.sockerSer = socket.socket(self.addrFamily,self.addrType)
        self.sockerSer.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.sockerSer.bind(address)
        self.sockerSer.listen(self.listenLine)

    def serverUp(self):
        while True:
            self.cli,self.cliAssr = self.sockerSer.accept()
            cliProcess = Process(target=self.handleReq)
            cliProcess.start()
            self.cli.close()

    def handleReq(self):
        recvdata = self.cli.recv(2014)
        lines = recvdata.splitlines()
        for line in lines:
            print(str(line,'utf-8'))

        headLine = lines[0]
        path = re.match('[^/]+(/[^ ]*)', str(headLine,'utf-8')).group(1)
        print('input path is [%s]'%path)
        if path =='/':
            path = rootPath + '/index.html'
        else:
            path = rootPath + path

        print('full path is [%s]'%path)

        try:
            flie = open(path)
        except IOError:
            self._responseHeaders = 'HTTP/1.1 404 not found\r\n'
            self._responseHeaders += '\r\n'
            self._responseBody = '===file not in path'
        else:
            self._responseHeaders = 'HTTP/1.1 200 OK\r\n'
            self._responseHeaders += '\r\n'
            self._responseBody = flie.read()
            flie.close()
        finally:
            response = self._responseHeaders + self._responseBody
            self.cli.send(bytes(response, 'utf-8'))
            self.cli.close()

serverPort = (HOST,PORT) = '',7788
rootPath = './html'

def makeServer(info):
    serve = WSGIServer(info)
    return serve
def main():
    httpd = makeServer(serverPort)
    print('http server created, port: %d'%PORT)
    httpd.serverUp()

if __name__ == '__main__':
    main()







