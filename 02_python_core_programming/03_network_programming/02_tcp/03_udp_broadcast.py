# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 12:39
# @Author  : Lim Yoona
# @Site    : 
# @File    : 03_udp_broadcast.py
# @Software: PyCharm

"""
    UDP广播
"""

"""
    网络编程中的广播
"""
import socket, sys

dest = ('<broadcast>', 7788)

# 创建套接字
so = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 设置广播
so.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# 发送数据
so.sendto(bytes('hi','utf-8'), dest)

print('等待对方回复（按Ctrl+C推出）')
while True:
    (buf, addr) = so.recvfrom(2048)
    print('received from %s: %s' % (addr, buf))
