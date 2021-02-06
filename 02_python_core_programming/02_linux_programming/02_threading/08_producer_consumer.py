# -*- coding: utf-8 -*-
# @Time    : AD 2021/02/03 21:14
# @Author  : Lim Yoona
# @Site    : 
# @File    : 08_producer_consumer.py
# @Software: PyCharm


"""
    生产者消费者模式

    1.队列：先进先出
    2.栈：先进后出

    python的Queue模块提供了同步和线程安全的队列类
        FIFO（先进先出）：Queue
        LIFO（后进先出）：LifoQueue
        优先级队列：PriorityQueue
"""

import threading,time

from queue import Queue

class Producer(threading.Thread):
    def run(self):
        global queue
        count = 0
        while True:
            if queue.qsize() <1000:
                for i in range(100):
                    count = count + i
                    msg = self.name +' 生产产品 '+ str(count)
                    queue.put(msg)
                    print(msg)
            time.sleep(0.5)


class Consumer(threading.Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize() > 100:
                for i in range(3):
                    msg = self.name + ' 消费产品 (' + queue.get()+')'
                    print(msg)

            time.sleep(1)



if __name__ == '__main__':
    queue = Queue()

    # for i in range(500):
    #     queue.put('初始化产品'+ str(i))

    for i in range(2):
        p = Producer()
        p.start()

    for i in range(5):
        c = Consumer()
        c.start()




"""
    总结：
        1.Queue在线程间的通信很重要
        2.往队列添加数据：put()
        3.从队列获取数据：get()
        4.判断队列是否有数据：qsize()

        通过阻塞队列，对消费者生产者模式进程解耦
"""