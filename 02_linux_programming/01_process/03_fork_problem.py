# -*- coding: utf-8 -*-
# @Time    : AD 2021/02/03 
# @Author  : Lim Yoona
# @Site    : 
# @File    : 03_fork_problem.py
# @Software: PyCharm

"""
    多次调用fork问题

    当调用一次fork函数，此时当前会出现父子两进程，在执行的过程中
    又一次执行了fork函数，这时候会在父子各自进程再开辟出两进程（父子进程）
    所以每执行一次fork，所产生的新的进程数是 2^n
    但是对于父子进程的执行顺序完全取决于操作系统的调度算法
"""

import os
import time

pid = os.fork()
if pid == 0:
    print("哈哈1")
else:
    print("哈哈2")


pid = os.fork()
if pid == 0:
    print("哈哈3")
else:
    print("哈哈4")

time.sleep(1)