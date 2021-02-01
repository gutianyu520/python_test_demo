#  coding=utf-8


"""
    迭代器：迭代器是一个可以记住遍历的位置的对象。迭代器对象从集合的第一个元素开始访问，
           直到所有的元素被访问完结束。迭代器只能往前不会后退
    作用对象：
        1.集合数据类型，如 list 、 tuple 、 dict 、 set 、 str 等
        2.generator ，包括生成器和带 yield 的generator function

    凡是可作用于 for 循环的对象都是 Iterable 类型；
    凡是可作用于 next() 函数的对象都是 Iterator 类型
    集合数据类型如 list 、 dict 、 str 等是 Iterable 但不是 Iterator ，不过可以通过 iter() 函数获得一个 Iterator 对象。


"""
from collections.abc import Iterable, Iterator

"""
    01_判断是否可以迭代
         isinstance() 
"""
print(isinstance([], Iterable))
print(isinstance((), Iterable))
print(isinstance({}, Iterable))
print(isinstance("[]", Iterable))
print(isinstance((x for x in range(5)), Iterable))
print(isinstance(100, Iterable))


"""
    02_迭代器_Iterator
"""
print("========================================")
print(isinstance([], Iterator))
print(isinstance((), Iterator))
print(isinstance({}, Iterator))
print(isinstance("[]", Iterator))
print(isinstance((x for x in range(5)), Iterator))
print(isinstance(100, Iterator))

"""
    03_iter()函数
        生成器都是 Iterator 对象，但 list 、 dict 、 str 虽然是 Iterable ，却不是 Iterator 。
        把 list 、 dict 、 str 等 Iterable 变成 Iterator 可以使用 iter() 函数
"""
print("========================================")
print(isinstance(iter([]), Iterator))
print(isinstance(iter(()), Iterator))
print(isinstance(iter({}), Iterator))
print(isinstance(iter("[]"), Iterator))
print(isinstance((x for x in range(5)), Iterator))
print(isinstance(100, Iterator))



