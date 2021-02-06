# -*- coding: utf-8 -*-
# @Time    : AD 2021/02/03 15:43
# @Author  : Lim Yoona
# @Site    : 
# @File    : 05_process_subclass.py
# @Software: PyCharm


"""
    Process子类
        继承Process类
        重写init方法
        重写run方法
        外部创建对象并且执行
"""

from multiprocessing import Process
import time
import os

class Sub_Process(Process):

    #重写初始化方法
    def __init__(self,interval):
        Process.__init__(self)
        self.interval = interval

    #重写run方法
    def run(self):
        print('子进程（%d）开始执行, 父进程id为（%d）' % (os.getpid(),os.getppid()))
        t_start = time.time()
        time.sleep(self.interval)
        t_stop = time.time()
        print('(%s)子进程执行结束，耗时%0.2f秒'%(os.getpid(),t_stop-t_start))

if __name__ == '__main__':
    t_start = time.time()
    print('当前进程（%s）'% os.getpid())
    p1 = Sub_Process(2)
    #没有target的情况下，执行start会调用run
    p1.start()
    p1.join()
    t_stop = time.time()
    print('(%s)执行结束，耗时%0.2f'%(os.getpid(),t_stop-t_start))





