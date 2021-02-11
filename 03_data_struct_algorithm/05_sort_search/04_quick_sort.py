# -*- coding: utf-8 -*-
# @Time    : 上午11:32
# @Author  : gutianyu
# @Site    : 
# @File    : 04_quick_sort
# @Software: PyCharm

"""快速排序QuickSort"""

"""
    快排又称划分交换排序（partition-exchange sort），将要排序的序列分割成独立的两部分，一组中的所有数据都要比另一组的
    所有数据要小，以此类推，递归进行，达到整个数据变成有序序列
    
    步骤：
        1.选出一个元素作为基准（pivot）
        2.重新排列，将比这元素大和小的划分两侧（partition）
        3.递归将两个子序列进行排序
        
    时间复杂度：
        最优时间复杂度：O(nlogn)
        最坏时间复杂度：O(n2)
        稳定性：不稳定
"""


def quick_sort(list, start, end):
    if start >= end:
        return
    mid = list[start]
    low = start
    high = end
    while low < high:
        while low < high and list[high] >mid:
            high -= 1
        list[low] = list[high]
        while low < high and list[low] < mid:
            low += 1
        list[high] = list[low]
    list[low] = mid
    quick_sort(list, start, low-1)
    quick_sort(list,low+1, end)

alist = [54,26,93,17,77,31,44,55,20]
quick_sort(alist, 1, len(alist)-1)
print(alist)





