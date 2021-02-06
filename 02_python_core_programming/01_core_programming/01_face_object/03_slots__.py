#  coding=utf-8

class Person(object):
    __slots__ = ("name", "age")

p = Person()
p.name="xiaoming"
p.age=14
#  p.score=13
"""
    使用slots限定属性个数之后就无法进行追加了，
    ★仅对当前类有效，对于子类无法进行约束
"""