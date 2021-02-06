# -*- coding: utf-8 -*-
# @Time : 2021/02/02 16:29
# @Author : Lim Yoona
# @Site : 
# @File : 07_functools.py
# @Software: PyCharm


"""
    functools
"""

"""
    functools 是python2.5被引人的,一些工具函数放在此包里
"""

"""
    partial函数(偏函数)
        把一个函数的某些参数设置默认值，返回一个新的函数，调用这个新函数会更简单。
"""

import functools


def test(*args, **kwargs):
    print(args)
    print(kwargs)


p = functools.partial(test, 1, 2, 3)
p()
print("*" * 20)
p(6, 7)
print("*" * 20)
p(name='a')

"""
    wraps函数
        注意：被修饰后的函数已经是另一个函数了（函数名等属性发生了变化）
        Python的functools包中提供了一个叫wraps的装饰器来消除这样的副作用
"""
print("=" * 20)


def note(func):
    @functools.wraps(func)  # 消除这样的副作用
    def wrapper():
        "wrapper function"
        print("hhhh")
        return func()

    return wrapper


@note
def test1():
    "test function"
    print("test1")


test1()
print(test1.__doc__)

















