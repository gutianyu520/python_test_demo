# -*- coding: utf-8 -*-
# @Time    : 2021/2/10 18:49
# @Author  : Lim Yoona
# @Site    : 
# @File    : 03_insertion_sort.py
# @Software: PyCharm

"""插入排序（insertion sort）"""
"""
    原理：
        通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置插入，
        插入排序的实现，再从后向前扫描的过程中，需要反复把已排序的元素逐步向后挪位，为新的元素提供插入空间
    
    时间复杂度：
        最优时间复杂度：O(n)(升序排列，序列已经处于升序状态)
        最坏时间复杂度：O(n2)
        稳定性：稳定
"""


def insert_sort(alist):
    for i in range(1, len(alist)):
        for j in range(i, 0, -1):
            if alist[j]<alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]


alist = [54,26,93,17,77,31,44,55,20]
insert_sort(alist)
print(alist)