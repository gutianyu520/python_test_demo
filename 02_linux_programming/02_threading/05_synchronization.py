# -*- coding: utf-8 -*-
# @Time    : AD 2021/02/03 19:39
# @Author  : Lim Yoona
# @Site    : 
# @File    : 05_synchronization.py
# @Software: PyCharm


"""
    同步
        多个线程修改数据时，需要同步控制
    互斥锁
        锁定/非锁定
"""

"""
    threading.Lock
"""


import threading

#创建锁
#mutex = threading.Lock()
#锁定
#mutex.acquire([blocking])
#释放
#mutex.release()

"""
    acquire()中的参数blocking说明：
        1.blocking为True，则当前线程会阻塞，直到获取锁为止（默认值：True）
        2.False，当前线程不会阻塞
"""

from threading import Thread,Lock
import time
g_num = 0



def test1():
    global g_num
    for i in range(1000000):
        mutexf = mutex.acquire(True)
        if mutexf:
            g_num += 1
            mutex.release()
    print("----test1-----g_num= %d" % g_num)


def test2():
    global g_num
    for i in range(1000000):
        mutexf = mutex.acquire(True)
        if mutexf:
            g_num += 1
            mutex.release()
    print("----test2-----g_num= %d" % g_num)


mutex = Lock()

p1 = Thread(target=test1)
p1.start()
p2 = Thread(target=test2)
p2.start()


"""
    说明：
        acquire(True)：加锁阻塞
        release()：解锁

    总结：
        优点：保证线程安全
        缺点：
            1.效率大大降低
            2.存在多个锁的时候就有可能出现死锁
"""









