# -*- coding: utf-8 -*-
# @Time    : 2021/2/6 11:11
# @Author  : Lim Yoona
# @Site    : 
# @File    : 05_web_dynamic_server.py
# @Software: PyCharm

"""
    Web动态服务器-1
"""

import socket,sys,re
from multiprocessing import Process

class WSGIServer:
    addrFamily = socket.AF_INET
    addrType = socket.SOCK_STREAM
    listenLine = 5

    def __init__(self, address):
        self.sockerSer = socket.socket(self.addrFamily, self.addrType)
        self.sockerSer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sockerSer.bind(address)
        self.sockerSer.listen(self.listenLine)

        self.serName = 'localhost'
        self.serPort = address[1]

    def serverUp(self):
        while True:
            self.cli,self.cliAssr = self.sockerSer.accept()
            cliProcess = Process(target=self.handleReq)
            cliProcess.start()
            self.cli.close()

    def setApp(self, application):
        self.application = application

    def handleReq(self):
        recvdata = self.cli.recv(2014)
        lines = recvdata.splitlines()
        for line in lines:
            print(str(line,'utf-8'))

        headLine = lines[0]
        path = re.match('[^/]+(/[^ ]*)', str(headLine,'utf-8')).group(1)
        print('input path is [%s]' % path)
        if path[-3:] != '.py':
            if path =='/':
                path = rootPath + '/index.html'
            else:
                path = rootPath + path

            print('full path is [%s]' % path)

            try:
                file = open(path)
            except IOError:
                self._responseHeaders = 'HTTP/1.1 404 not found\r\n'
                self._responseHeaders += '\r\n'
                self._responseBody = '===file not in path'
            else:
                self._responseHeaders = 'HTTP/1.1 200 OK\r\n'
                self._responseHeaders += '\r\n'
                self._responseBody = file.read()
                file.close()
            finally:
                response = self._responseHeaders + self._responseBody
                self.cli.send(bytes(response, 'utf-8'))
                self.cli.close()
        else:
            env = {}
            bodyContent = self.application(env, self.startResponse)
            self.finishResponse(bodyContent)

    def startResponse(self, status, response_headers):
        serverHeaders = [
            ('Date', 'Tue, 31 Mar 2016 10:11:12 GMT'),
            ('Server', 'WSGIServer 0.2'),
        ]
        self.headers_set = [status, response_headers+serverHeaders]

    def finishResponse(self,bodyContent):
        try:
            status, response_headers = self.headers_set
            response = 'HTTP/1.1 {status}\r\n'.format(status = status)
            for header in response_headers:
                response += '{0}: {1}\r\n'.format(*header)
            response += '\r\n'
            for data in bodyContent:
                response += data
            self.cli.send(bytes(response, 'utf-8'))
        finally:
            self.cli.close()

serverPort = (HOST,PORT) = '',8888
rootPath = './html'
pyRoot = './wsgiPy'

def makeServer(serverPort, application):
    serve = WSGIServer(serverPort)
    serve.setApp(application)
    return serve

def main():
    if len(sys.argv) <2:
        sys.exit('请按照要求，指定模块名称:应用名称,例如 module:callable')

    appPath = sys.argv[1]
    moudle, application = appPath.split(':')
    sys.path.insert(0,pyRoot)
    print(sys.path)
    moudle = __import__(moudle)
    application = getattr(moudle,application)
    httpd = makeServer(serverPort,application)
    print('http server created, port: %d' % PORT)
    httpd.serverUp()

if __name__ == '__main__':
    main()











