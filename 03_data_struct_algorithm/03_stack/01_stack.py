# -*- coding: utf-8 -*-
# @Time    : 2021/2/10 16:33
# @Author  : Lim Yoona
# @Site    : 
# @File    : 01_stack.py
# @Software: PyCharm

"""
    栈（stack）
"""

"""
    栈是一种容器
        功能：
            插入元素
            访问元素
            删除元素
        特点：
            先进后出（LIFO）
"""

class Stack:
    def __init__(self):
        """
            初始化
        """
        self.items = []

    def is_empty(self):
        """
            返回是否为空
        :return:
        """
        return self.items ==[]

    def push(self, item):
        """
            插入元素
        :param item:
        :return:
        """
        self.items.append(item)

    def pop(self):
        """
            弹出元素
        :return:
        """
        return self.items.pop()

    def peek(self):
        """
            返回栈顶元素
        :return:
        """
        return self.items[len(self.items) - 1]

    def size(self):
        """
            返回栈大小
        :return:
        """
        return len(self.items)


if __name__ == '__main__':
    stack = Stack()
    stack.push('hello')
    stack.push('world')
    stack.push('enjoyEdu')
    print(stack.size())
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())













