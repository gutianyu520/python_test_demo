# -*- coding: utf-8 -*-
# @Time : 2021/02/01 17:26
# @Author : Lim Yoona
# @Site : 
# @File : 05_deepcopy_shallowcopy.py
# @Software: PyCharm

"""
    1. 浅拷贝 =
    浅拷贝是对于一个对象的顶层拷贝
    通俗的理解是：拷贝了引用，并没有拷贝内容
"""
a = [11,22,33]
b = a
print(id(a))
print(id(b))
b.remove(11)
print(id(a))
print(id(b))
print(a)
print(b)

"""
    2. 深拷贝
    深拷贝是对于一个对象所有层次的拷贝(递归)
"""
print("---------------------------")
import copy
a = [11,22,33]
c = copy.deepcopy(a)
print(id(a))
print(id(c))
print(a)
print(c)
c.append(44)
print(id(a))
print(id(c))
print(a)
print(c)

"""
    3. 拷贝的其他方式
    浅拷贝对不可变类型和可变类型的copy不同
"""
print("---------------------------")
a = [11,22,34]
d = copy.copy(a)
print(id(a))
print(id(d))
a.append(45)
print(a)
print(d)

print("---------------------------")

"""分片表达式可以赋值一个序列"""
a ='abc'
b = a[:]
"""字典的copy方法可以拷贝一个字典"""
d = dict(name= "hello",age = 13)
co = d.copy()
"""有些内置函数可以生成拷贝(list)"""
a = list(range(10))
print(a)
b = list(a)
"""copy模块中的copy函数"""
a = (11,22,33)
b = copy.copy(a)










