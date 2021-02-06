# -*- coding: utf-8 -*-
# @Time    : AD 2021/02/03 21:42
# @Author  : Lim Yoona
# @Site    : 
# @File    : 09_threadlocal.py
# @Software: PyCharm


"""
    ThreadLocal

    1.使用函数传参
        不能共享
    2.使用全局字典
        代码low
    3.threadlocal


    虽然threadlocal对于所有线程本身是都可见的，但是其实对于每个线程，
    里面的数据都是自己线程独有的，不会造成数据的混乱
    每个线程可以对threadlocal中的数据进行自己独特的处理
    threadlocal解决了一个线程在各个函数之间互相传递的问题


"""

import threading

local_school = threading.local()

def process_student():
    std= local_school.student
    print('hello, %s (in %s)'%(std,threading.current_thread().name))

def process_thread(name):
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread, args=('donge',),name= "Thread-A")
t2 = threading.Thread(target=process_thread, args=('老王',),name= "Thread-B")
t1.start()
t2.start()
t1.join()
t2.join()










