# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 20:32
# @Author  : Lim Yoona
# @Site    : 
# @File    : 07_coroutine.py
# @Software: PyCharm

"""
    协程：比线程还要小的执行单元，自带CPU上下文
"""
"""
    协程与线程的差异：
        线程切换更耗性能
        协程是单纯的操作CPU上下文
        
    协程的问题：
        协程需要手动进行CPU切换（让协程主动自己交出CPU的执行权）
    
    协程的好处：
        封装IO操作，适合高IO密集型
"""

import time

def A():
    while True:
        print("----A---")
        yield
        time.sleep(0.5)

def B(c):
    while True:
        print("----B---")
        c.next()
        time.sleep(0.5)

if __name__=='__main__':
    a = A()
    B(a)




