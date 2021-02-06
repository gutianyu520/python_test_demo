# -*- coding: utf-8 -*-
# @Time    : 2021/2/4 15:52
# @Author  : Lim Yoona
# @Site    : 
# @File    : 02_tcp_programming.py
# @Software: PyCharm
"""
    TFTP协议（Trivial File Transfer Protocol，简单文件传输协议）：
"""
"""
    特点：
        简单
        占用资源少
        适合传递小文件
        适合在局域网内进行传递
        端口号位69
        基于udp实现

    过程：
        1.监听69端口
        2.客户端发送下载请求
        3.服务端批准请求，使用新的临时端口进行数据传输
        4.文件进行多次发送（512字节-次）
        5.客户端收到数据包返回确认信息（应答包）

    TFTP数据包形式：
        1.请求：操作码+文件名+0+模式+0
        2.数据包：操作码+块编码+数据
        3.ack（应答包）：操作码+块编码
        4.ERROR：操作码+差错码+差错信息+0
"""

from socket import *
import struct, sys

ip = ''
if len(sys.argv) != 2:
    print('-' * 30)
    print('tips:')
    print('python 02_tcp.py 192.168.1.1')
    print('-' * 30)
    exit()
else:
    ip = sys.argv[1]

# 创建套接字
udpso = socket(AF_INET, SOCK_DGRAM)

cmd_buf = struct.pack("!H8sb5sb", 1, 'test.jpg', 0, "octet", 0)

sendAddr = (ip, 69)
udpso.sendto(cmd_buf, sendAddr)

p_num = 0
recvFile = ''
while True:
    recvData, recvAddr = udpso.recvfrom(1024)
    recvDataLen = len(recvData)
    cmdTuple = struct.unpack("!HH", recvData[:4])
    cmd = cmdTuple[0]
    currentPackNum = cmdTuple[1]
    if cmd == 3:
        if currentPackNum == 1:
            recvFile = open("test.jpg", 'a')

        if p_num + 1 == currentPackNum:
            recvFile.write(recvData[4:])
            p_num += 1
            print('(%d)次收到的数据' % p_num)
            ackBuf = struct.pack("!HH", 4, p_num)
            udpso.sendto(ackBuf, recvAddr)

        if recvDataLen < 516:
            recvFile.close()
            print('已经下载成功！！！')
            break
    elif cmd == 5:
        print('Error num:%d' % currentPackNum)
        break

udpso.close()
