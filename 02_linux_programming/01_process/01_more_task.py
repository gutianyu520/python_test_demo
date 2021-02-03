# -*- coding: utf-8 -*-
# @Time    : 2021/2/3 14:09
# @Author  : Lim Yoona
# @Site    : 
# @File    : 01_more_task.py
# @Software: PyCharm

import os

"""
    fork()进程的创建:
        1.程序执行到os.fork()时，操作系统会创建一个新的进程（子进程），然后复制父进程的所有信息到子进程中
        2.然后父进程和子进程都会从fork()函数中得到一个返回值，在子进程中这个值一定是0，而父进程中是子进程的 id号
    fork()函数只能在linux的系统上使用
"""
pid = os.fork()

if pid == 0:
    print("1")
else:
    print("2")

"""
    getpid()：获取子进程的id
    getppid()：获取父进程的id
"""

rpid = os.fork()
if rpid < 0:
    print("fork调用失败")
elif rpid == 0:
    print("我是子进程（%d），我的父进程（%d）" % (os.getpid(), os.getppid()))
else:
    print("我是父进程（%d），我的子进程（%d）" % (os.getpid(), rpid))
print("父子进程都可以执行的代码")