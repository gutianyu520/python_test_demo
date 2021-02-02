# -*- coding: utf-8 -*-
# @Time : 2021/02/02 14:58
# @Author : Lim Yoona
# @Site : 
# @File : 03_gc_model.py
# @Software: PyCharm

"""垃圾回收(三)-gc模块"""

"""
    一.垃圾回收机制：引用计数为主，分代收集为辅
        1.导致引用计数+1的情况
            1.1 对象被创建
            1.2 引用
            1.3 作为参数传递
            1.4 作为元素存储在容器中，例：list
        
        2.导致引用计数+1的情况
            2.1 对象别名显示销毁，del
            2.2 对象别名被赋值新对象
            2.3 离开作用域，函数体内的局部变量
            2.4 对象所在容器被销毁
        
        3.查看引用计数
"""
# import sys
#
# a = "hello world"
# print(sys.getrefcount(a))


"""
    二.循环引用导致内存泄露
    略
"""

"""
    三.垃圾回收
    下面的代码执行完的最后结果
        -----0------
        object born,id:0x1e3699a1fd0
        object born,id:0x1e3699a1fa0
        -----1------
        -----2------
        []
        -----3------
        4
        -----4------
        [<__main__.ClassA object at 0x000001E3699A1FD0>, <__main__.ClassA object at 0x000001E3699A1FA0>, {'t': <__main__.ClassA object at 0x000001E3699A1FA0>}, {'t': <__main__.ClassA object at 0x000001E3699A1FD0>}]
        -----4------
        
        结论：
            1.垃圾回收后的对象存放在gc.garbage列表中
            2.gc.collect()返回不可达的对象的数目，除对象本身以外还有其对应的字典dict
"""
import gc


class ClassA():
    def __init__(self):
        print('object born,id:%s' % str(hex(id(self))))


def fun3():
    print("-----0------")
    c1 = ClassA()
    c2 = ClassA()
    c1.t = c2
    c2.t = c1
    print("-----1------")
    del c1
    del c2
    print("-----2------")
    print(gc.garbage)
    print("-----3------")
    print(gc.collect())
    print("-----4------")
    print(gc.garbage)
    print("-----4------")


if __name__ == '__main__':
    gc.set_debug(gc.DEBUG_LEAK)
    fun3()

"""
    触发垃圾回收的条件：
        1.调用gc.collect()
        2.引用计数到达阈值
        3.程序退出
"""


"""
    四.gc模块常用功能解析
        主要应用：解决循环引用问题
    
        常用函数：
            1.gc.set_debug(flags)：设置gc的debug日志，一般设置为gc.DEBUG_LEAK
            2.gc.collect([generation])：显式进行垃圾回收，0，1，2或者不填（表全查），检查对应代的对象，返回不可达对象数目
            3.gc.get_threshold()：获取的gc模块中自动执行垃圾回收的频率
            4.gc.set_threshold([threshold0], [threshold1], [threshold2])：设置自动执行垃圾回收的频率
            5.gc.get_count()：获取当前自动执行垃圾回收的计数器，返回一个长度为3的列表
        
        gc模块的自动垃圾回收机制
            条件：引入gc模块，开启自动回收：is_enable()=true
            
            作用：发现并处理不可达的对象
            
            过程：垃圾检查+垃圾回收
        
        注意点：
            gc模块唯一处理不了的就是__del__方法，因此要避免定义__del__方法
"""