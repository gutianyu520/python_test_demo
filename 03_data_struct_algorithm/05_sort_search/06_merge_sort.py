# -*- coding: utf-8 -*-
# @Time    : 下午4:03
# @Author  : gutianyu
# @Site    : 
# @File    : 06_merge_sort
# @Software: PyCharm

"""归并排序"""
"""
    归并排序是采用分而治之的一个典型的应用
    思想：
        先递归分解数组，再合并数组
    步骤：
        数组分解最小之后，进行合并两有序数组，比较两个数组最前面的数，谁小就先取谁，
        取后相应的指针往后移一位
    
    时间复杂度：
        最优时间复杂度：O(nlogn)
        最坏时间复杂度：O(nlogn)
        稳定性：稳定
"""

def merger_sort(list):
    if len(list) <= 1:
        return list
    num = len(list)//2
    left = merger_sort(list[:num])
    right = merger_sort(list[num:])
    return merge(left, right)


def merge(left, right):
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result

list = [54,26,93,17,77,31,44,55,20]
list = merger_sort(list)
print(list)









