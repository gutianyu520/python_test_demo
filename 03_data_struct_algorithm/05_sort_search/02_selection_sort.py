# -*- coding: utf-8 -*-
# @Time    : 2021/2/10 17:31
# @Author  : Lim Yoona
# @Site    : 
# @File    : 02_selection_sort.py
# @Software: PyCharm


"""
    选择排序（selection sort）    
""""""
    工作原理：
        先找到最小（大）元素，排在队列起始位置，再从剩余未排序与元素中继续寻找最小（大）元素，然后放在已排序序列的末尾，直至所有元素排序完毕
    特点：
        数据移动与其位置有关，若出现在正确的位置上，则不会移动

    时间复杂度：
        最优时间复杂度：O(n2)
        最坏时间复杂度：O(n2)
        稳定性：不稳定
"""

def selection_sort(alist):
    n = len(alist)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if alist[j]<alist[min_index]:
                min_index = j
        if min_index != 1:
            alist[i], alist[min_index] = alist[min_index], alist[i]


alist = [54, 226, 93, 17, 77, 31, 44, 55, 20]
selection_sort(alist)
print(alist)














