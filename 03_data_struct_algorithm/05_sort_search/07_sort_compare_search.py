# -*- coding: utf-8 -*-
# @Time    : 下午4:22
# @Author  : gutianyu
# @Site    : 
# @File    : 07_sort_compare_search
# @Software: PyCharm

"""
    常见排序算法比较：
"""
"""
    排序方法    平均情况            最好情况    最坏情况         辅助空间    稳定性
    冒泡排序    O(n2)              O(n)         O(n2)       O(1)       稳定
    选择排序    O(n2)               O(n2)       O(n2)       O(1)        不稳定
    插入排序    O(n2)               O(n)        O(n2)       O(1)        稳定
    希尔排序    O(nlogn)~O(n2)      O(n1.3)     O(n2)       O(1)        不稳定
    堆  排序    O(nlogn)           O(nlogn)    O(nlogn)    O(1)        不稳定
    归并排序    O(nlogn)            O(nlogn)    O(nlogn)    O(1)        稳定
    快速排序    O(nlogn)            O(nlogn)    O(n2)       O(1)        不稳定
"""

"""
    搜索
        常见方法：顺序查找、二分查找、二叉树查找、哈希查找
    
    二分查找（半查找）：
        优点：
            比较次数少，查找速度块，平均性能好
        缺点：
            要求待查表为有序表，且插入删除困难
        适用对象：
            不经常变动而查找频繁的有序列表
"""

"""非递归实现"""

def binary_search(alist, item):
    f = 0
    l = len(alist) -1
    while f <= l:
        mid = (f + l) //2
        if alist[mid] == item:
            return True
        elif item <alist[mid]:
            l = mid -1
        else:
            f = mid +1
    return False
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binary_search(testlist, 3))
print(binary_search(testlist, 13))





"""递归实现"""

def binary_search_recursion(alist, item):
    if len(alist) == 0:
        return False
    else:
        mid = len(alist) // 2
        if alist[mid] == item:
            return True
        else:
            if item< alist[mid]:
                return binary_search_recursion(alist[:mid], item)
            else:
                return binary_search_recursion(alist[mid+1:], item)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binary_search_recursion(testlist, 3))
print(binary_search_recursion(testlist, 13))


