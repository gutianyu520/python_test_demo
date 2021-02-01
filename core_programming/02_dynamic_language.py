# coding:utf-8


"""
    python是动态语言
    运行时可以改变其结构
"""
import types


class Person(object):
    taller = "100mi"

    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def eat(self):
        print("eat food")


p = Person("小明", 24)
print(p.name)
print(p.age)

"""
    01_动态给实例绑定属性
"""
p.sex = "male"
print(p.sex)

"""
    02_动态给类绑定(添加)方法
"""

p.eat()


def run(self, speed):
    print("%s 以每秒%dm/s速度行走" % (self.name, speed))


p.run = types.MethodType(run, p)
p.run(30)

"""
    03_绑定类方法、绑定静态方法
"""


@classmethod
def cry(cls):
    print("%s is crying" % (cls.taller))


@staticmethod
def owl():
    print("hhhhhhhhh")


Person.cry = cry  # 绑定类方法
Person.owl = owl  # 绑定静态方法

Person.cry()
Person.owl()


"""
    动态删除属性、方法
    删除的方法:
        1.del 对象.属性名
        2.delattr(对象, "属性名")
        
    相对于动态语言，静态语言具有严谨性！所以，玩动态语言的时候，小心动态的坑！
    请使用__slots__
"""



