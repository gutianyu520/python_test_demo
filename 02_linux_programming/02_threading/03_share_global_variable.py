# -*- coding: utf-8 -*-
# @Time    : AD 2021/02/03 19:06
# @Author  : Lim Yoona
# @Site    : 
# @File    : 03_share_global_variable.py
# @Software: PyCharm

"""
    多线程-共享全局变量

"""

from  threading import Thread
import time

g_num = 100

def work1():
    global g_num
    for i in range(3):
        g_num += 1

    print('-----in work1 , g_num = %d' % g_num)


def work2():
    global g_num
    print('-----in work2 , g_num = %d' % g_num)

print('---- before creating thread g_num is  %d ' % g_num)

t1 = Thread(target= work1)
t1.start()
time.sleep(1)

t2 = Thread(target= work2)
t2.start()


"""
    列表当作实参传递到线程中
"""

def work3(nums):
    nums.append(44)
    print('-----in work3 ' , nums)


def work4(nums):
    time.sleep(1)
    print('-----in work4 ' , nums)

g_nums = [11,22,33]

t3 = Thread(target= work3,args=(g_nums,))
t3.start()

t4 = Thread(target= work4,args=(g_nums,))
t4.start()



"""
    总结：
        1.一个进程内的所有线程共享全局变量
        2.线程非安全
"""