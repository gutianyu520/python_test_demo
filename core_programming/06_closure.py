# coding=utf-8

"""
    函数引用
"""


# 创建函数
def test1():
    print('test1')


# 调用函数
test1()

# 引用函数
ret = test1
print(id(ret))
print(id(test1))

# 通过引用调用函数
ret()


# 闭包
def test(num):
    # 创建内部函数，通过外部传递参数到内部函数实现闭包
    def test_in(num_in):
        print("in test_in 函数, number_in is %d" % num_in)
        return num + num_in

    return test_in


rep = test(20)

print(rep(100))


def counter(start=0):
    count = [start]

    def incr():
        count[0] += 1
        return count[0]

    return incr


ret2 = counter(5)
print(ret2())
print(ret2())

print("-------------------------------------------")


"""
闭包思考：
    1.闭包似优化了变量，原来需要类对象完成的工作，闭包也可以完成
    2.由于闭包引用了外部函数的局部变量，则外部函数的局部变量没有及时释放，消耗内存
"""

def linr_add(a, b):
    def line(x):
        return a * x + b

    return line

ret3 = linr_add(1,2)
print(ret3(3))
print(ret3(4))
