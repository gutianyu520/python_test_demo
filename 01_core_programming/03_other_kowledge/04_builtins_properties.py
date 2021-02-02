# -*- coding: utf-8 -*-
# @Time : 2021/02/02 15:41
# @Author : Lim Yoona
# @Site : 
# @File : 04_builtins_properties.py
# @Software: PyCharm

"""内建属性"""


# class Person(object): 经典类
#     pass

class Person:  # py3中已默认继承object
    pass


print(dir(Person))

"""
    python3.9中的内建属性和方法：
        ['__class__', 
        '__delattr__', 
        '__dict__', 
        '__dir__', 
        '__doc__', 
        '__eq__', 
        '__format__', 
        '__ge__', 
        '__getattribute__', 
        '__gt__', 
        '__hash__', 
        '__init__', 
        '__init_subclass__', 
        '__le__', 
        '__lt__', 
        '__module__', 
        '__ne__', 
        '__new__', 
        '__reduce__', 
        '__reduce_ex__', 
        '__repr__', 
        '__setattr__', 
        '__sizeof__', 
        '__str__', 
        '__subclasshook__', 
        '__weakref__']
    
"""

"""
    常用专有属性      	说明 	                触发方式
    __init__ 	        构造初始化函数 	        创建实例后,赋值时使用,在__new__后
    __new__ 	        生成实例所需属性 	        创建实例时
    __class__ 	        实例所在的类 	            实例.__class__
    __str__ 	        实例字符串表示,可读性 	    print(类实例),如没实现，使用repr结果
    __repr__ 	        实例字符串表示,准确性 	    类实例 回车 或者 print(repr(类实例))
    __del__ 	        析构 	                del删除实例
    __dict__ 	        实例自定义属性 	        vars(实例.__dict__)
    __doc__ 	        类文档,子类不继承 	    help(类或实例)
    __getattribute__ 	属性访问拦截器 	        访问实例属性时
    __bases__ 	        类的所有父类构成元素 	    类名.__bases__
    
    需要注意：__getattribute__的坑
        不要在__getattribute__方法中调用self.xxx，会导致死循环问题
"""


