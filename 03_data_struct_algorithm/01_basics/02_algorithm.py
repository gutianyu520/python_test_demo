# -*- coding: utf-8 -*-
# @Time    : 2021/2/7 9:39
# @Author  : Lim Yoona
# @Site    : 
# @File    : 02_algorithm.py
# @Software: PyCharm


"""
    算法
"""
"""
    算法的概念
        算法是计算机处理信息的本质
        
    算法是独立存在的一种解决问题的方法和思想。
    
    五大特性:
        1.输入：0个或多个输入
        2.输出：1个或多个输出
        3.有穷性：有限的步骤后自动结束，每一步在可接受时间内完成
        4.确定性：每一步含义确定，无歧义
        5.可行性：每一步都是可行的，执行有限次数完成
        
    算法效率衡量：
        执行时间即可反应算法效率，即算法的优劣（单单靠时间无法作为标准，需要靠计算机硬件和操作系统的支持）
"""
import time

start = time.time()
for a in range(0, 1001):
    for b in range(0, 1001 - a):
        c = 1000 - a - b
        if a ** 2 + b ** 2 == c ** 2:
            print('a , b, c = %d, %d, %d' % (a, b, c))

end = time.time()
print('cost time is %f' % (end - start))
print('completed')








