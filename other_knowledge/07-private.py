# -*- coding: utf-8 -*-
# @Time : 2021/02/01 17:52
# @Author : Lim Yoona
# @Site : 
# @File : 07-private.py
# @Software: PyCharm

"""
    私有化
"""

"""
    
    xx: 公有变量
    _x: 单前置下划线,私有化属性或方法，from somemodule import *禁止导入,类对象和子类可以访问
    __xx：双前置下划线,避免与子类中的属性命名冲突，无法在外部直接访问(名字重整所以访问不到)
    __xx__:双前后下划线,用户名字空间的魔法对象或属性。例如:__init__ , __ 不要自己发明这样的名字
    xx_:单后置下划线,用于避免与Python关键词的冲突

"""