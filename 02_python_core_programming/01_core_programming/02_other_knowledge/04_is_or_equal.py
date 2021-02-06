# -*- coding: utf-8 -*-
# @Time : 2021/02/01 17:18
# @Author : Lim Yoona
# @Site : 
# @File : 04_is_or_equal.py
# @Software: PyCharm

"""
    这里是关于==、is的辨析问题
"""

import copy

a = [11,22,33]
b = a
print(a == b)
print(a is b)

c = copy.deepcopy(a)
print(a == c)
print(a is c)


"""
    ==：表示的是两个比较对象的值是否相等
    is：表示的是两个比较对象指向是否是同一个
"""





