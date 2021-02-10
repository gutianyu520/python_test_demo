# -*- coding: utf-8 -*-
# @Time    : 2021/2/10 17:09
# @Author  : Lim Yoona
# @Site    : 
# @File    : 01_bubble_sort.py
# @Software: PyCharm

"""
    冒泡排序
""""""
    比较两个元素，不符合排序要求的则调换两者顺序，遍历整个队列直至排序完成
    
    算法运作：
        1.比较相邻的元素。如果第一个比第二个大（升序），就交换他们两个。
        2.对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
        3.针对所有的元素重复以上的步骤，除了最后一个。
        4.持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。 

    时间复杂度：
        最优时间复杂度：O(n)
        最坏时间复杂度：O(n2)
        稳定性：稳定
    
"""


def bubble_sort(alist):
    for j in range(len(alist)-1, 0, -1):
        for i in range(j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]


li = [54, 23, 56, 98, 22, 45]
bubble_sort(li)
print(li)






