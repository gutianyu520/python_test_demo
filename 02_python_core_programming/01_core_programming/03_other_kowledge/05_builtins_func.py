# -*- coding: utf-8 -*-
# @Time : 2021/02/02 15:53
# @Author : Lim Yoona
# @Site : 
# @File : 05_builtins_func.py
# @Software: PyCharm

"""
    内建函数
"""
from functools import reduce

"""
    range 
        range(stop)
        range(start,stop,step)
        注意上述只适用于数值,返回一个list
 
"""
a = range(5)
print(list(a))
b = range(1, 5, 2)
print(list(b))

"""    
    map
        map(...)
            map(func,param...,)
        
        map的第一个参数是function，第二个参数是function中需要的参数，返回值是一个list
        
"""

a = map(lambda x: x + 1, [1])

print(a.__next__())

"""
    filter：指定序列进行过滤操作
        filter(func or None,param)
            func:接收一个参数，返回true或false
            param: list，元组或string
"""


def test(param):
    if param == 1:
        return True
    else:
        return False


a = filter(test, [1, 2, 3, 4])
print(list(a))

"""
    reduce(python3中，该函数不属于内建函数，需要functools)
        reduce(func,param,initial)
            func:函数有两个参数
            param:str，tuple，list
            initial:固定初始值
"""


def add(x, y):
    return x + y


print(reduce(add, [1, 2, 3, 4], 5))


"""
    sorted
        sorted(iterable, cmp=None, key=None, reverse=False)
"""

print(sorted([22,34,11,33],reverse=1))


