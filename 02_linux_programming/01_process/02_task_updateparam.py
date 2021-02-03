# -*- coding: utf-8 -*-
# @Time    : 2021/2/3 14:28
# @Author  : Lim Yoona
# @Site    : 
# @File    : 02_task_updateparam.py
# @Software: PyCharm


"""
    多进程修改全局变量

    多进程中，每个进程所有的数据（包括全局变量）都是进程唯一的，不存在共享修改
"""

import os
import time

num = 0

pid = os.fork()

if pid == 0:
    num += 1
    print('哈哈1----num=%d'%num)
else:
    time.sleep(1)
    num +=1
    print('哈哈2----num=%d'%num)
