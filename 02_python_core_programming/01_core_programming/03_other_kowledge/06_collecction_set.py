# -*- coding: utf-8 -*-
# @Time : 2021/02/02 16:19
# @Author : Lim Yoona
# @Site : 
# @File : 06_collecction_set.py
# @Software: PyCharm


"""集合set"""

"""
    集合与之前列表、元组类似，可以存储多个数据，但是这些数据是不重复的
    集合对象还支持:
        union(联合) 
        intersection(交) 
        difference(差)
        sysmmetric_difference(对称差集)
        ...数学运算
"""
a = set('abc dd')
b = set('abe')
print(a)
print(type(a))

print(a & b)  # 交集
print(a | b)  # 并集
print(a - b)  # 差集
print(a ^ b)  # 对称差集(不会同时出现在二者中)
