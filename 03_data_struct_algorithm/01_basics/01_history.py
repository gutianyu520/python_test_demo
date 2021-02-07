# -*- coding: utf-8 -*-
# @Time    : 2021/2/7 9:25
# @Author  : Lim Yoona
# @Site    : 
# @File    : 01_history.py
# @Software: PyCharm

""""""
"""
    案例：如果 a+b+c=1000，且 a^2+b^2=c^2（a,b,c 为自然数），如何求出所有a、b、c可能的组合?
"""

import time

start = time.ctime()
for a in range(0,1001):
    for b in range(0,1001):
        for c in range(0,1001):
            if a ** 2 + b ** 2 == c ** 2 & a + b + c == 1000:
                print('a , b, c = %d, %d, %d' % (a, b, c))

end = time.ctime()
print('cost time is %f' % (end - start))
print('completed')