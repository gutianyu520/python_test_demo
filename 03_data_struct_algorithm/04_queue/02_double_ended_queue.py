# -*- coding: utf-8 -*-
# @Time    : 2021/2/10 16:52
# @Author  : Lim Yoona
# @Site    : 
# @File    : 02_double_ended_queue.py
# @Software: PyCharm

"""
    双端队列（deque，double-ended queue）
"""
"""
    具有队列和栈的性质的数据结构
    双端队列的任意一端入队和出队
"""

class Deque:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_first(self, item):
        self.items.insert(0, item)

    def add_pail(self, item):
        self.items.append(item)

    def remove_first(self):
        return self.items.pop(0)

    def remove_pail(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    deque = Deque()
    deque.add_first(1)
    deque.add_first(2)
    deque.add_pail(6)
    deque.add_pail(8)
    print(deque.size())
    print(deque.items)
    print(deque.remove_first())
    print(deque.remove_pail())

























