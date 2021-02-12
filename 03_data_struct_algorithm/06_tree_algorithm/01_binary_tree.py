# -*- coding: utf-8 -*-
# @Time    : 下午4:43
# @Author  : gutianyu
# @Site    : 
# @File    : 01_binary_tree
# @Software: PyCharm

"""树(tree)"""

"""
    树是一种抽象的数据类型（ADT）或是数据结构，用于模拟具有树状结构性质的数据集合。
    
    特点：
        1.每个节点有零个或多个子节点
        2.没有父节点的节点称为根节点
        3.每一个非根节点有且只有一个父节点
        4.除了根节点以外，每个子节点可以分为多个不相交的子树
    
    术语：
        1.节点的度：资格节点含有的子树的个数
        2.树的度：一棵树中最大的节点的度
        3.叶节点(终端节点)：度为0的节点
        4.父亲节点(父节点)：含有子节点的节点，对于该子节点而言，称为父节点
        5.孩子节点(子节点)：含有父节点的节点，对于该父节点而言，称为子节点
        6.兄弟节点：含有相同父节点的节点，称为兄弟节点
        7.节点的层次：根为第一层，其子节点为第二层，以此类推
        8.树的高度(深度)：树中节点的最大层次
        9.堂兄弟节点：父节点在同一层的节点互为堂兄弟
        10.节点的祖先：从根到该节点所经分支上的所有节点
        11.子孙：以某个节点为根的子树中任一节点都成为该节点的子孙
        12.森林：有n棵互不相交的树的集合
    
    树的种类：
        1.无序树(自由树)：树中任意节点的子节点之间没有顺序关系
        2.有序树：树中的任意子节点之间有顺序关系
            二叉树：每个节点最多只有两个子树的树
                完全二叉树：对于一棵深度为d的树，除d层，其他各层的节点数目达到最大值，第d层所有节点从左向右紧密排列
                    满二叉树：所有的叶节点都在最底层的完全二叉树
                平衡二叉树(AVL树)：有且仅当任何节点的两棵子树的高度差不大于1
                排序二叉树：二叉查找树，二叉搜索树，有序二叉树
            霍夫曼树(最优二叉树)：带权路径最短的二叉树
            B树：对于读写操作进行优化的自平衡的二叉查找树，保持数据有序，子树数量大于2
            
    树的存储：
        顺序存储
        链式存储
    
    应用场景：
        1.xml，html解析
        2.路由协议
        3.mysql数据索引
        4.文件系统的目录结构
        5.AI算法
"""

"""
    二叉树：
        子树分为左子树和右子树
        
        特性：
            1.第i层上至多有 2^(i-1)个节点
            2.深度为k的树，最多 2^k -1个节点
            3.任一二叉树，叶节点数为N0，而度数为2的节点总数为N2，N0=N2+1
            4.n个节点的完全二叉树的深度为log2(n+1)
            5.对于完全二叉树，从上往下，从左往右编号，第i个节点，其左子节点必为2i，右子节点必为2i+1，其双亲的编号必为i/2（根节点除外）
"""


class Node:
    def __init__(self, elem=-1, lChild=None, rChild=None):
        self.elem = elem
        self.lChild = lChild
        self.rChild = rChild


class Tree:
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








