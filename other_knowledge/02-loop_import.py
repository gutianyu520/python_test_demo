# -*- coding: utf-8 -*-
# @Time : 2021/02/01 17:00
# @Author : Lim Yoona
# @Site : 
# @File : 02-loop_import.py
# @Software: PyCharm

"""
    导入外部文件
"""

"""
    当两个py文件中互相引用的对象的函数，
    并且在对应的函数里调到自己的方法，就会导致循环导入的问题
"""

from core_programming import hello
hello.hello()

"""
    2. 怎样避免循环导入
        1.程序设计上分层，降低耦合
        2.导入语句放在后面需要导入时再导入，例如放在函数体内导入
"""