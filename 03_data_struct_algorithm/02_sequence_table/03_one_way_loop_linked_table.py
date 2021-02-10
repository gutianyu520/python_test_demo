# -*- coding: utf-8 -*-
# @Time    : 2021/2/10 15:12
# @Author  : Lim Yoona
# @Site    : 
# @File    : 03_one_way_loop_linked_table.py
# @Software: PyCharm

"""单向循环链表"""

"""
    链表的最后一个节点的next指向链表的头节点
"""


class Node:
    def __init__(self,item):
        self.item = item
        self.next = None


class SinCycLinkedList:
    def __init__(self):
        """
            初始化
        """
        self._head = None

    def is_empty(self):
        """
            判断是否为空
        :return:
        """
        return self._head == None

    def length(self):
        """
            返回链表长度
        :return:
        """
        if self._head == None:
            return 0
        count = 1
        cur = self._head
        while cur.next != self._head:
            count += 1
            cur = cur.next

        return count

    def travel(self):
        """
            链表遍历
        :return:
        """
        if self.is_empty():
            return
        cur = self._head
        print(cur.item)
        while cur.next != self._head:
            cur = cur.next
            print(cur.item)
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
            node.next = self._head
        else:
            node.next = self._head
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
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
            node.next = self._head
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
            node.next = self._head

    def insert(self, pos, item):
        """
            按下标插入元素
        :param pos: 下标
        :param item: 元素
        :return:
        """
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() -1):
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            count = 0
            while count < (pos -1):
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        """
            删除元素
        :param item:
        :return:
        """
        if self.is_empty():
            return
        cur = self._head
        pre = None
        if cur.item == item:
            if cur.next != self._head:
                while cur.next != self._head:
                    cur = cur.next
                cur.next = self._head.next
                self._head = self._head.next
            else:
                self._head = None
        else:
            pre = self._head
            while cur.next != self._head:
                if cur.item == item:
                    pre.next = cur.next
                    return
                else:
                    pre = cur
                    cur = cur.next
            if cur.item == item:
                pre.next = cur.next

    def search(self, item):
        """
            返回链表中是否存在元素
        :param item:
        :return:
        """
        if self.is_empty():
            return False
        cur = self._head
        if cur.item == item:
            return True
        while cur.next != self._head:
            cur = cur.next
            if cur.item == item:
                return True
        return False


if __name__ == '__main__':
    ll = SinCycLinkedList()
    ll.add(1)
    ll.add(2)
    ll.append(5)
    ll.insert(1, 9)
    print("length :", ll.length())
    ll.travel()
    print(ll.search(1))
    print(ll.search(3))
    ll.remove(1)
    print("length: ", ll.length())
    ll.travel()









