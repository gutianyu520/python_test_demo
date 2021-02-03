# -*- coding: utf-8 -*-
# @Time    : AD 2021/02/03 20:56
# @Author  : Lim Yoona
# @Site    : 
# @File    : 07_deadlock.py
# @Software: PyCharm

"""
    死锁：
        定义：线程间共享多个资源，若两个线程分别占有一部分资源并同时等待对方的资源，就会造成死锁
"""


from threading import Thread,Lock
import time

class MyThread1(Thread):
    def run(self):
        if mutexA.acquire():
            print(self.name + '-----do1---up----')
            time.sleep(1)

            if mutexB.acquire():
                print(self.name + '-----do1---down----')
                mutexB.release()

            mutexA.release()


class MyThread2(Thread):
    def run(self):
        if mutexB.acquire():
            print(self.name + '-----do2---up----')
            time.sleep(1)

            if mutexA.acquire():
                print(self.name + '-----do2---down----')
                mutexA.release()

            mutexB.release()

mutexA = Lock()
mutexB = Lock()

if __name__ == '__main__':
    t1 = MyThread1()
    t2 = MyThread2()
    t1.start()
    t2.start()



"""
    解决方案：
        1.程序设计尽量避免（银行家算法）
        2.添加超时时间


    线程同步：使用互斥锁完成多个任务，有序的进程任务，就是线程同步
"""