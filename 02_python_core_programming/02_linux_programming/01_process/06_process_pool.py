# -*- coding: utf-8 -*-
# @Time    : AD 2021/02/03 15:56
# @Author  : Lim Yoona
# @Site    : 
# @File    : 06_process_pool.py
# @Software: PyCharm



"""
    进程池 pool
    需要注意的是：不能直接将35以后的代码放在py文件中，这个执行需要在__main__中执行

    创建过程：
        创建：p = Pool(进程数)
        执行：p.apply_async(函数名,参数元组,参数字典)
        关闭：p.close()

"""



from multiprocessing.pool import Pool
import os,time,random

def worker(msg):
    t_start = time.time()
    print('%s 开始执行，进程号为%d'%(msg,os.getpid()))
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg,'执行完毕，耗时%0.2f'%(t_stop-t_start))



if __name__ == '__main__':

    po = Pool(3)

    for x in range(0,10):
        po.apply_async(worker,(x,))
        # po.apply(worker,(x,))


    print('-------start-------')
    po.close()
    po.join()
    print('-------end-------')


"""
    multiprocesing.Pool常用的函数：
        apply_async(func,args,kwargs):非阻塞方式调用func
        apply(func,args,kwargs):阻塞式调用func
        close():关闭Pool，不再接收新的任务
        terminate():强制终止
        join():主进程阻塞，等待子进程结束，必须在close或ternimate之后使用
"""








