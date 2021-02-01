# coding=utf-8


"""
    ★（根本不用关系元类的使用，因为基本上使用不到，所以元类了解就可以了）
    元类的用处：
        1.拦截类的创建
        2.修改类
        3.返回修改之后的类


"""


"""
 01_类的创建
"""


class ObjectCreator(object):
    pass


my_object = ObjectCreator()

print(my_object)

"""
   02_类打印,在python中类也可以作为对象进行传输
"""
print(ObjectCreator)

"""
    03_判断类是否含有某个属性
"""
print(hasattr(ObjectCreator, 'name'))

"""
    04_动态给类添加属性
"""
ObjectCreator.name = 'foo'
print(hasattr(ObjectCreator, 'name'))

"""
    05_将类赋值变量
"""
obj = ObjectCreator
print(obj())

"""
   06_动态创建类，返回的是类，而不是类的实例
    使用class关键字时，python解释器会自动创建对象
"""


def createObj(name):
    if name == 'foo':
        class Foo(object):
            pass

        return Foo
    else:
        class Bar(obj):
            pass

        return Bar


print(createObj('foo'))
print(createObj('foo1'))
print("---------------------------------------------")
print(type(ObjectCreator()))

"""
    07_使用type创建类
    type(类名, 由父类名称组成的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)
"""
Test = type("Test", (), {'age': 14})
print(Test())

Test2 = type("Test2", (Test,), {'name': 'hello'})
print(Test2())

test2 = Test2()
print(Test2.name)
print(Test2.age)

"""
    08_添加静态方法
"""


@staticmethod
def staticMethod():
    print("this is a static method")


Test3 = type('Test3', (Test2,), {'staticMethod': staticMethod})

Test3.staticMethod()

"""
    09_添加类方法
"""


@classmethod
def classMethod(cls):
    print(cls.age)


Test4 = type('Test4', (Test2,), {'staticMethod': staticMethod, 'classMethod': classMethod})
test4 = Test4()
test4.classMethod()

"""
    10_元类就是用来创建类的“东西”。
    元类就是类的类,函数type实际上是一个元类
"""
print(Test4.__class__)
tol = True
print(tol.__class__.__class__)
print(my_object.__class__.__class__)

"""
    11_ __metaclass__属性
    在类中使用__metaclass__属性，就表明着这个类是使用元类进行创建类对象,
    python会在当前类找，在父类找，没有找到时则使用type
"""

print("==============================================><====================================")

"""
    12_自定义元类
"""


def create_class_meta(future_class_name, future_class_parents, future_class_attr):
    newAttr = {}
    for name, value in future_class_attr.items():
        if not name.startswith("__"):
            newAttr[name.upper()] = value

    return type(future_class_name, future_class_parents, newAttr)


class Foo(object, metaclass=create_class_meta):
    # __metaclass__ = create_class_meta (python2中的写法)
    bar = 'bip'


print(hasattr(Foo, 'bar'))
print(hasattr(Foo, 'BAR'))

f = Foo()
print(f.BAR)
