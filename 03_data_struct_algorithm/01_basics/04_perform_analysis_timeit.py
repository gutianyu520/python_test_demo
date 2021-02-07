# -*- coding: utf-8 -*-
# @Time    : 2021/2/7 10:41
# @Author  : Lim Yoona
# @Site    : 
# @File    : 04_perform_analysis_timeit.py
# @Software: PyCharm

"""Python内置类型性能分析"""
"""
    timeit模块可以用来测试一小段Python代码的执行速度
"""
from timeit import Timer

"""
    Timer:测量小段代码执行速度的类
    def __init__(self, stmt="pass", setup="pass", timer=default_timer,globals=None):
    stmt:要测试的代码语句
    setup:运行代码时需要的参数
    timer: 定时器函数
"""


def test1():
    l = []
    for i in range(1000):
        l = l + [i]


def test2():
    l = []
    for i in range(1000):
        l.append(i)


def test3():
    l = [i for i in range(1000)]


def test4():
    l = list(range(1000))


t1 = Timer('test1()', 'from __main__ import test1')
t2 = Timer('test2()', 'from __main__ import test2')
t3 = Timer('test3()', 'from __main__ import test3')
t4 = Timer('test4()', 'from __main__ import test4')

print('concat : ', t1.timeit(number=1000), ' s')
print('append : ', t2.timeit(number=1000), ' s')
print('comprehension : ', t3.timeit(number=1000), ' s')
print('list range : ', t4.timeit(number=1000), ' s')


x = list(range(200000))
pop_0 = Timer('x.pop(0)', 'from __main__ import x')
print('pop_0 : ', pop_0.timeit(number=100000), ' s')

y = list(range(200000))
pop = Timer('y.pop()', 'from __main__ import y')
print('pop : ', pop.timeit(number=100000), ' s')
