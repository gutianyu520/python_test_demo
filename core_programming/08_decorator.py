# coding=utf-8

# 装饰器
def foo():
    print('foo')


# 表示函数
foo
# 表示调用函数
foo()

foo = lambda x: x + 1
# 此时fool指向另外一个lambda的函数表达式，而不是原来的函数了
print(foo(10))
print("---------------------------------")

"""
    装饰器的实际应用案例
"""
def decorator_fool(func):
    def inner():
        print("this is decorator method")
        func()
    return inner

@decorator_fool
def foo1():
    print("fool1")

foo1()

"""
    python中的装饰器有点类似于Java中的aop，将原来的方法进行增强这样不需要对原方法进行修改，就能达到一样的效果。
    装饰器(decorator)功能
    
    1.引入日志
    2.函数执行时间统计
    3.执行函数前预备处理
    4.执行函数后清理功能
    5.权限校验等场景
    6.缓存


    1.当有参数的函数需要调用时如下，将内部函数带上参数，
      这样再将该参数传给被装饰的函数就行了
    2.被修饰函数可以带有返回值，没有影响
"""
def timecunt(func):
    def ti(a,b):
        print(a+b)
        func(a,b)
    return ti

@timecunt
def ttt(a,b):
    print("jjjjjjjjjj")

ttt(1,2)





