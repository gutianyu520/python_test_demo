# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 21:03
# @Author  : Lim Yoona
# @Site    : 
# @File    : 09_gevent_coroutine.py
# @Software: PyCharm
from gevent import monkey
import gevent
from urllib import request

"""
    协程--gevent
        在greenlet基础上实现了自动切换
        
    调用gevent.sleep()实现自由切换
"""


def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(0.5)


g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)
g1.join()
g2.join()
g3.join()

"""
    gevent并发下载器
"""
monkey.patch_all()


def download(url):
    print("GET: %s" % url)
    resp = request.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s' % (len(data), url))


download('http://www.baidu.com/')
gevent.joinall(
    [gevent.spawn(download, 'http://www.baidu.com/'),
     gevent.spawn(download, 'http://www.itcast.cn/'),
     gevent.spawn(download, 'http://www.itheima.com/'), ]
)
