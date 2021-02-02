#  coding=utf-8


"""
    在Python中，这种一边循环一边计算的机制，称为生成器：generator
    生成器的特点：
        1.节约内存
        2.迭代到下一次的调用时，所使用的参数都是第一次所保留下的，
        即是说，在整个所有函数调用的参数都是第一次所调用时保留的，而不是新创建的
    ★用途：列表创建
"""

"""
    01_创建生成器方法1
    列表生成式的 [ ] 改成 ( )
"""

s1 = [x*2 for x in range(5)]
print(s1)  # [0, 2, 4, 6, 8]

s2 = (x*2 for x in range(5))
print(s2)  # <generator object <genexpr> at 0x000002718A40F190>

"""
    s1是一个列表，s2是一个生成器，s2输出使用next()
"""
print(next(s2))
print(next(s2))
print(next(s2))
print(next(s2))
print(next(s2))

"""
    生成器保存的是算法，每次调用 next(G) ，就计算出 G 的下一个元素的值，
    直到计算到最后一个元素，没有更多的元素时，抛出 StopIteration 的异常
"""

"""
    02_创建生成器方法2
        用函数来实现
        ：斐波那契数列
            for循环调用generator时，发现拿不到generator的return语句的返回值。
            如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
"""
def fib(times):
    n = 0
    a,b = 0,1
    while n < times:
        yield b
        a,b = b,a+b
        n+=1
    return "done"

f = fib(5)
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
print("=====================")
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.send('haha'))
print(f.__next__())
# print(f.__next__())









