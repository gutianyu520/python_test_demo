# -*- coding: utf-8 -*-
# @Time    : 2021/2/10 16:01
# @Author  : Lim Yoona
# @Site    : 
# @File    : 04_two_way_linked_table.py
# @Software: PyCharm

"""
    双向链表
"""


class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.pre = None


class DLinkedList:
    """
        初始化
    """
    def __init__(self):
        self._head = None

    def is_empty(self):
        """
            返回链表是否为空
        :return:
        """
        return self._head == None

    def length(self):
        """
            返回链表长度
        :return:
        """
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """
            遍历链表
        :return:
        """
        cur = self._head
        while cur != None:
            print(cur.item)
            cur = cur.next
        print("")

    def add(self, item):
        """
            头插法
        :param item:
        :return:
        """
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            node.next = self._head
            self._head.pre = node
            self._head = node

    def append(self, item):
        """
            尾插法
        :param item:
        :return:
        """
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.pre = cur

    def search(self, item):
        """
            是否存在元素
        :param item:
        :return:
        """
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

    def insert(self, pos, item):
        """
            在指定下标插入元素
        :param pos: 下标
        :param item: 元素
        :return:
        """
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            count = 0
            while count < (pos -1):
                count += 1
                cur = cur.next
            node.pre = cur
            node.next = cur.next
            cur.next.pre = node
            cur.next = node

    def remove(self, item):
        """
            删除指定元素
        :param item:
        :return:
        """
        if self.is_empty():
            return
        else:
            cur = self._head
            if cur.item == item:
                if cur.next == None:
                    self._head = None
                else:
                    cur.next.pre = None
                    self._head = cur.next
                return
        while cur != None:
            if cur.item == item:
                cur.pre.next = cur.next
                cur.next.pre = cur.pre
                break
            cur = cur.next


if __name__ == '__main__':
    ll = DLinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(13)
    ll.append(6)
    ll.insert(1, 90)
    print("length : ", ll.length())
    ll.travel()
    print(ll.search(1))
    print(ll.search(62))
    ll.remove(1)
    print("length ： ", ll.length())
    ll.travel()

















