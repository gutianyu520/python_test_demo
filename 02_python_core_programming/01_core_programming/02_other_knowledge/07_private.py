# -*- coding: utf-8 -*-
# @Time : 2021/02/01 17:52
# @Author : Lim Yoona
# @Site : 
# @File : 07_private.py
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


class Person(object):
    def __init__(self, name, age, taste):
        self.name = name
        self._age = age
        self.__taste = taste

    def showPerson(self):
        print(self.name)
        print(self._age)
        print(self.__taste)

    def doWork(self):
        self._work()
        self.__away()

    def _work(self):
        print('do work')

    def __away(self):
        print('my __away')


class Student(Person):
    def construction(self, name, age, taste):
        self.name = name
        self._age = age
        self.__taste = taste

    def showStudent(self):
        print(self.name)
        print(self._age)
        print(self.__taste)

    @staticmethod
    def testBug():
        _Bug.showBug()


class _Bug(object):

    @staticmethod
    def showBug():
        print("show bug")

s1 = Student('xiaoli',12,'football')
s1.showPerson()
print('*'*20)

'''
    构造函数调用到父类的私有属性，会报错，找到该属性
'''
#s1.showStudent()

s1.construction('xiawang',34,'basketball')
s1.showPerson()
print('*'*20)

s1.showStudent()
print('*'*20)
Student.testBug()


"""
    总结  
        1.父类中属性名为__名字的，子类不继承，子类不能访问
        2.如果在子类中向__名字赋值，那么会在子类中定义的一个与父类相同名字的属性
        3._名的变量、函数、类在使用from xxx import *时都不会被导入

"""
