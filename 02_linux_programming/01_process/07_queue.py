# -*- coding: utf-8 -*-
# @Time    : AD 2021/02/03 16:49
# @Author  : Lim Yoona
# @Site    : 
# @File    : 07_queue.py
# @Software: PyCharm


"""
    进程间通信-Queue
    queue实现进程之间的通信
"""


""" queue使用"""

from multiprocessing import Queue,Process
import time,random
# q = Queue(3)
# q.put('消息1')
# q.put('消息2')
# print(q.full())
# q.put('消息3')
# print(q.full())

# try:
#     q.put('消息4',True,2)
# except:
#     print("消息队列已满，现有消息数量%d" % q.qsize())
#
# try:
#     q.put_nowait('消息5')
# except:
#     print("消息队列已满，现有消息数量%d" % q.qsize())

# print(q.qsize())
# if not q.full():
#     q.put_nowait('消息6')
#
# if not q.empty():
#     for i in range(q.qsize()):
#         #这条代码在mac中执行不了 Raises NotImplementedError on Mac OSX because of broken sem_getvalue()
#         print(q.get_nowait())


"""
    函数说明：
        qsize():返回当前队列包含的消息数量（mac无法执行）
        empty():队列为空返回True，反之返回False
        full():队列满了返回True，反之返回False
        get(block,[timeout]):获取队列中的一条消息，并将其移出队列，block默认True
            1.block使用默认值，消息队列为空时，阻塞，直到有消息为止，设置timeout，等待指定时间后抛异常（Queue Empty）
            2.设置为false，则当消息队列为空直接抛异常（Queue Empty）
        put_nowait(item): = put(item,False)
"""


"""
    Queue实例
"""

def write(quo):
    for val in ['A','B','C']:
        print('Put %s to queue...' % val)
        quo.put(val)
        time.sleep(random.random())

def read(quo):
    while True:
        if not quo.empty():
            val = quo.get(True)
            print('read %s from queue..' % val)
            time.sleep(random.random())
        else:
            break


if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=write,args=(q,))
    p2 = Process(target=read,args=(q,))

    p1.start()
    p1.join()
    p2.start()
    p2.join()
    print('')
    print('数据已读完。。。')


"""
    若采用进程池中的Queue，则需要将multiprocess.Queue 改成 multiprocess.Manager
    使用Manager中的Queue
        Manager.Queue()
"""







