# -*- coding: utf-8 -*-
# @Time    : 2021/2/10 16:45
# @Author  : Lim Yoona
# @Site    : 
# @File    : 01_queue.py
# @Software: PyCharm

"""
    队列（queue）
"""
"""
    数据结构：
        先进先出（FIFO）
"""


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.size())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
















