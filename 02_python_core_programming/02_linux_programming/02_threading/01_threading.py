# -*- coding: utf-8 -*-
# @Time    : AD 2021/02/03 18:40
# @Author  : Lim Yoona
# @Site    : 
# @File    : 01_threading.py
# @Software: PyCharm


"""
    多线程-threading

    1.使用threading模块
"""

import threading,time

def saySorry():
    print('darling, i am so sorry, can i have dinner?')
    time.sleep(1)

if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=saySorry)
        t.start()
        print('current thrading count : %d' % len(threading.enumerate()))

    time.sleep(2)
    print('current thrading count : %d' % len(threading.enumerate()))
    print('main theading is close')

"""
    2.主线程等待子线程结束后才结束
"""

"""
    3.查看线程数

    len(threading.enumerate())
"""









