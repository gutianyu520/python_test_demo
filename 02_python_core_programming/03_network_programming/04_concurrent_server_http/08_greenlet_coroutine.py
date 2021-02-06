# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 20:58
# @Author  : Lim Yoona
# @Site    : 
# @File    : 08_greenlet_coroutine.py
# @Software: PyCharm

from greenlet import greenlet
import time
"""
    协程的封装（greenlet）
"""

def test1():
    while True:
        print('----A----')
        gr2.switch()
        time.sleep(0.5)


def test2():
    while True:
        print('----B----')
        gr1.switch()
        time.sleep(0.5)


gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()
