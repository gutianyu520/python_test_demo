# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 19:06
# @Author  : Lim Yoona
# @Site    : 
# @File    : 05_select_single_server.py
# @Software: PyCharm


"""
    单进程服务器（select）
"""

"""
  多路复用模型：
    select
        优点：几乎所有平台都支持
        缺点：
            1.单个进程能够监视的文件描述符的数量存在最大限制，linux 1024
            2.对socket进行扫描采用轮询方式进行扫描，效率低
            3.套接字较多时，都要通过遍历来完成调度，浪费了CPU调度  
"""

import select, socket, sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 7788))
s.listen(5)
inputs = [s]

running = True
while True:
    # 调用select函数，阻塞等待
    readable, writeable, exp = select.select(inputs, [], [])
    # 数据抵达，循环
    for sock in readable:
        # 监听到新的连接
        if sock == s:
            conn, addr = sock.accept()
            inputs.append(conn)
        # 监听到键盘输入
        elif sock == sys.stdin:
            cmd = sys.stdin.readline()
            running = False
            break
        # 数据到达
        else:
            data = sock.recv(1024)
            if data:
                str1= str(data,'utf-8')+"hh"
                sock.send(bytes(str1,'utf-8'))
                print(str(data))
            else:
                inputs.remove(sock)
                sock.close()
    if not running:
        break

s.close()
