# -*- coding: utf-8 -*-
# @Time    : AD 2021/02/03 18:51
# @Author  : Lim Yoona
# @Site    : 
# @File    : 02_attention_points.py
# @Software: PyCharm


"""
    threading注意点

    1.线程执行代码的封装（新建class继承threading.Thread,重写run）
"""
import threading,time

class MyThread(threading.Thread):

    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "i m " + self.name + " @ " + str(i)
            print(msg)


if __name__ == '__main__':
    for i in range(5):
        t = MyThread()
        t.start()


"""
    2.线程的执行顺序
        执行顺序属于无序
"""

"""
    3.总结
        1.每个线程都会有名字，python主动为线程指定一个名字
        2.run方法结束代表线程结束
        3.无法控制线程的执行顺序，可以通过其它方式影响线程的调度（sleep的时间长度）
        4.线程的集中状态：新建-就绪-等待-运行-死亡
"""








