# -*- coding: utf-8 -*-
# @Time    : 2021/2/13 19:13
# @Author  : Lim Yoona
# @Site    : 
# @File    : 03_redis_senior.py
# @Software: PyCharm

"""redis高级"""

"""
    发布订阅:
        消息格式:
            消息类型:
                subscribe:订阅成功
                unsubscribe:取消订阅成功
                message:其他终端发布消息
        
        命令:
            1.订阅:subscribe <channel> <channel>...
            2.取消订阅:unsubscribe <channel> <channel>...
            3.发布:publish <channel> <message>
    
    主从配置:
        设置主服务器配置:bind 192.168.1.10
        设置从服务器配置:
            bind 192.168.1.11
            slaveof 192.168.1.10 6379
        master写数据:set hello world
        slave读数据:get hello
"""

# 引入模块
import redis

r = None
# 连接
try:
    r = redis.StrictRedis(host='192.168.0.144', port=6379)
except Exception as e:
    print(e.__doc__)

# 方式一:直接进去读写
r.set('name', 'hello')
print(str(r.get('aa'), 'utf-8'))

# 方式二:pipline
pipe = r.pipeline()
pipe.set('name', 'world')
print(pipe.get('name'))
pipe.execute()


#封装
class RedisHelper:
    def __init__(self, host='localhost', port=6379):
        self._redis = redis.StrictRedis(host=host, port=port)

    def get(self, key):
        if self._redis.exists(key):
            return self._redis.get(key)
        else:
            return ''

    def set(self, key, value):
        self._redis.set(key, value)



