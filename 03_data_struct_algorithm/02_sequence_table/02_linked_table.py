# -*- coding: utf-8 -*-
# @Time : 2021/02/09 17:59
# @Author : Lim Yoona
# @Site : 
# @File : 02_linked_table.py
# @Software: PyCharm

"""
    链表:充分利用计算机内存空间，实现灵活的内存动态管理
"""
"""
    定义：常见的基础数据结构，是一种线性表，每个节点存放下一个节点的位置信息（地址）
    
    单向链表（单链表）：
        最简单的链表表现形式
        节点：存放 信息域（元素域） + 链接域（指向下一个节点，最后一个节点的链接域指向空值）
            1.表元素域存放具体数据
            2.链接域存放下一个节点的位置
            3.变量指向链表的头节点，以此可以找到表中任意节点
    
    链表与顺序表的对比：
        操作                链表                顺序表
        访问元素             O(n)                O(1)   
        头部插入/删除         O(1)               O(n)
        尾部插入/删除         O(n)               O(1)
        中部插入/删除         O(n)               O(n)
    
    注意：虽然表面看起来复杂度都是 O(n)，但是链表和顺序表在插入和删除时进行的是完全不同的操作。
        链表的主要耗时操作是遍历查找，删除和插入操作本身的复杂度是O(1)。顺序表查找很快，主要耗时的操作是拷贝覆盖。
        因为除了目标元素在尾部的特殊情况，顺序表进行插入和删除时需要对操作点之后的所有元素进行前后移位操作，
        只能通过拷贝和覆盖的方法进行。
"""

# 实现


class SingleNode:
    """单向链表"""
    def __init__(self, item):
        self.item = item
        self.next = None


"""
    操作：
        1.is_empty()
        2.length()
        3.travel():遍历链表
        4.add(item)
        5.append(item)        
        6.insert(pos,item)
        7.remove(item)
        8.search(item)
"""


class SingleLinkedList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head == None

    def length(self):
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self._head
        while cur != None:
            print(cur.item)
            cur = cur.next
        print("")

    """头部添加元素"""
    def add(self, item):
        node = SingleNode(item)
        node.next = self._head
        self._head = node

    """尾部添加元素 """
    def append(self, item):
        node = SingleNode(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self,pos,item):
        if pos < 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            node = SingleNode(item)
            count = 0
            pre = self._head
            while count < (pos -1):
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def remove(self,item):
        cur = self._head
        pre = None
        while cur != None:
            if cur.item == item:
                if not pre:
                    self._head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self,item):
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False


"""测试"""

if __name__ == '__main__':
    ll = SingleLinkedList()
    ll.add(1)
    ll.travel()
    print()
    ll.append(2)
    ll.travel()
    print()
    ll.insert(1, 4)
    ll.travel()
    print()
    ll.remove(4)
    ll.travel()
    print()
    print(ll.search(2))
    print(ll.search(3))


