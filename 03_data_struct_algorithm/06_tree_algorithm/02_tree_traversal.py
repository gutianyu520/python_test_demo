# -*- coding: utf-8 -*-
# @Time    : 2021/2/12 10:58
# @Author  : Lim Yoona
# @Site    : 
# @File    : 02_tree_traversal.py
# @Software: PyCharm

"""二叉树遍历"""
"""
    深度优先：递归
        先序遍历
        中序遍历
        后序遍历
    广度优先：队列
"""


class Node:
    def __init__(self, elem=-1, lChild=None, rChild=None):
        self.elem = elem
        self.lChild = lChild
        self.rChild = rChild



class tree:
    def __init__(self, root=None):
        self.root = root

    def add(self, elem):
        node = Node(elem)
        if self.root == None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            while queue:
                cur = queue.pop(0)
                if cur.lChild == None:
                    cur.lChild =node
                    return
                elif cur.rChild ==None:
                    cur.rChild = node
                    return
                else:
                    queue.append(cur.lChild)
                    queue.append(cur.rChild)

    """深度优先算法"""
    def pre_order(self, root):
        """先序遍历"""
        if root == None:
            return
        print(root.elem)
        self.pre_order(root.lChild)
        self.pre_order(root.rChild)

    def mid_order(self, root):
        """中序遍历"""
        if root == None:
            return
        self.mid_order(root.lChild)
        print(root.elem)
        self.mid_order(root.rChild)

    def post_order(self, root):
        """后续遍历"""
        if root == None:
            return
        self.mid_order(root.lChild)
        self.mid_order(root.rChild)
        print(root.elem)

    """广度优先算法"""
    def breadth_travel(self,root):
        if root == None:
            return
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            print(node.elem)
            if node.lChild != None:
                queue.append(node.lChild)
            if node.rChild != None:
                queue.append(node.rChild)



