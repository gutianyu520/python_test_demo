# -*- coding: utf-8 -*-
# @Time    : 下午3:46
# @Author  : gutianyu
# @Site    : 
# @File    : 05_shell_sort
# @Software: PyCharm

"""希尔排序（shell sort）"""
"""
    也称增量缩小排序，是插入排序的改进版，属于非稳定算法
    
    过程：
        将数组列在一个表中并对列分别进行插入排序，重复此过程
        
    时间复杂度：
        最优时间复杂度：根据补偿序列的不同而不同
        最坏时间复杂度：O(n2)
        稳定性：不稳定
"""

def shell_sort(list):
    n= len(list)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            j = i
            while j >= gap and list[j-gap] > list[j]:
                list[j-gap], list[j] = list[j], list[j-gap]
                j -= gap

        gap = gap // 2

list = [54,26,93,17,77,31,44,55,20]
shell_sort(list)
print(list)













