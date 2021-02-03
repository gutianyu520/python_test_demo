# -*- coding: utf-8 -*-
# @Time    : AD 2021/02/03 15:18
# @Author  : Lim Yoona
# @Site    : 
# @File    : 04_multiprocessing.py
# @Software: PyCharm

"""
    由于fork()只是linux平台上使用的，为了对于跨平台的支持，提供了multiprocessing模块（跨平台版本）
"""

from multiprocessing import Process
import os

def run_proc(name):
    print("子进程运行中，name= %s , pid = %d ..." % (name, os.getpid()))

if __name__ == '__main__':
    print('父进程 %d. ' % os.getpid())
    p = Process(target=run_proc, args= ('test',))
    print('子进程将要执行')
    p.start()
    p.join() #保证子进程执行完成后执行后面的代码
    print('子进程结束')

'''
    process创建子进程过程：
        1.传入执行的函数和函数中所需参数
        2.创建一个Process实例
        3.使用start()启动
        4.join():保证子进程执行完成后执行后面的代码
'''


"""
    Process语法结构：
    Process([group],[target],[name],[args],[kwargs])
        target:调用函数
        args:被调用函数中所需参数元组
        kwargs:被调用函数中的字典
        name:当前进行实例别名
        group:基础上用不到

    常用方法：
        is_alive():判断进程实例是否在执行
        join([time]):是否等待进程实例执行结束，或等多少秒
        start():启动进程实例
        run():没有给定target参数的情况下，调用start方法实际上会去执行run方法
        terminate():强制终止当前进程

    常用属性：
        name:当前进程别名，默认Process-N,N从1开始累加的整数
        pid:当前进程pid

"""







