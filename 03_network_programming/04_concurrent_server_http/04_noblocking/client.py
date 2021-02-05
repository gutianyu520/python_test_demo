# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 18:41
# @Author  : Lim Yoona
# @Site    : 
# @File    : client.py
# @Software: PyCharm

from socket import *
import random
import time

g_cli = []
for i in range(10):
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('192.168.159.1', 7788))
    g_cli.append(s)
    print(i)

while True:
    for s in g_cli:
        s.send(bytes(random.randint(0, 100)))
        time.sleep(0.5)