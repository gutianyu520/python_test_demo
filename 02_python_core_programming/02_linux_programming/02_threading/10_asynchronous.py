# -*- coding: utf-8 -*-
# @Time    : AD 2021/02/03 21:55
# @Author  : Lim Yoona
# @Site    : 
# @File    : 10_asynchronous.py
# @Software: PyCharm


"""
    异步
"""

from multiprocessing import Pool
import time,os
def test():
    print('---进程池中的进程---pid = %d ,ppid = %d'%(os.getpid(),os.getppid()))
    for i in range(3):
        print('------%d--------'% i)
        time.sleep(1)
    return "haha"

def test2(args):
    print('---callback func ---pid = %d'%os.getpid())
    print('---callback func ---args = %s'%args)


if __name__ == '__main__':
    p = Pool(3)
    p.apply_async(func = test,callback = test2)
    time.sleep(5)

    print('------主进程-pid = %d -----'% os.getpid())






