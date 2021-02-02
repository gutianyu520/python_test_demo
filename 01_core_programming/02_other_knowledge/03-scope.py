# -*- coding: utf-8 -*-
# @Time : 2021/02/01 17:08
# @Author : Lim Yoona
# @Site : 
# @File : 03-scope.py
# @Software: PyCharm


"""作用域"""

"""
    locals()函数用于打印局部变量
    globals()函数用于打印全局变量
"""
A = 100
B = 100

"""
    通过global标签，可以在函数体内进行声明全局变量
"""
def test():
    global a
    a = 11
    b = 22
    print(locals())


test()
print(globals())


"""
    内建模块（builtins）
    俗称默认函数，不需要额外导入就可以直接使用的函数
    例：dict，list，type，print
"""