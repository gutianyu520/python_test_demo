# -*- coding: utf-8 -*-
# @Time : 2021/02/02 11:52
# @Author : Lim Yoona
# @Site : 
# @File : 08_property.py
# @Software: PyCharm


"""属性 property"""
"""1. 私有属性添加getter和setter方法"""


class Money(object):
    def __init__(self):
        self.__money = 0

    def getMoney(self):
        return self.__money

    def setMoney(self, val):
        if isinstance(val, int):
            self.__money = val
        else:
            print("传输的不是整数类型")

    money = property(getMoney, setMoney)  # 往下看


"""2. 使用property升级getter和setter方法"""
a = Money()
print(a.money)
a.money = 100
print(a.money)
print(a.getMoney())

"""3. 使用property取代getter和setter方法"""
print('*'*20)

class Weight(object):
    def __init__(self):
        self.__weight = 0

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, val):
        if isinstance(val, int):
            self.__weight = val
        else:
            print("is not int")


b = Weight()
print(b.weight)
b.weight = 200
print(b.weight)