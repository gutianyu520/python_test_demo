# -*- coding: utf-8 -*-
# @Time    : 2021/2/13 16:51
# @Author  : Lim Yoona
# @Site    : 
# @File    : 02_redis_basic.py
# @Software: PyCharm

"""数据库操作"""
"""
    redis属于key-value数据
        key:字符串
            1.查找键:keys <pattern>
            2.检查键是否存在，存在返回1，没有返回0（当查询多个键时，返回的是结果累加）:exists <key> <key>...
            3.查看对应键的值类型:type <key>
            4.删除键值对:del <key> <key>...
            5.设置超时: expire <key> <seconds>
            6.查看键的有效时间:ttl <key>
        value:
            字符串string:
                设置:
                    1.设置:set <key> <value>
                    2.设置超时:SETEX <key> <seconds> <value>
                    3.设置多个值:MSET <key> <value> <key> <value>...
                获取:
                    1.获取:get <key>
                    2.获取多个: mget <key> <key> ...
                运算(前提:值为数字):(执行完后会将结果存储到value中)
                    1.value+1:INCR <key>
                    2.value+n:INCRBY <key> <increment>
                    3.value-1:DECR <key>
                    4.value-n:DECRBY <key> <decrement>
                其他:
                    1.追加值(往原值后面进行字符串拼接，返回值的长度):append <key> <value>
                    2.获取值长度:strlen <key>
            哈希hash:
                设置:
                    1.设置单个属性:hset <key> <field> <value>
                    2.设置多个属性:hset <key> <field> <value> <field> <value>...
                获取:
                    1.获取一个属性的值:hget <key> <field>
                    2.获取多个属性的值:hmget <key> <field> <field>...
                    3.获取所有属性和值:hgetall key
                    4.获取所有属性的值:hkeys key
                    5.返回包含属性的个数:hlen key
                    6.获取所有值:hvals key
                其他:
                    1.判断属性是否存在:hexists <key> <field>
                    2.删除属性及值:hdel <key> <field> <field>...
                    3.返回值的字符串长度:hstrlen <key> <field>
            列表list:
                设置:
                    1.头部插入数据:lpush <key> <value> <value>...
                    2.尾部插入数据:rpush <key> <value> <value>...
                    3.在一个元素的前|后插入新元素:linsert <key> before|after <pivot:目标值> <value>
                    4.对于指定的位置设置值(下标基于0，-1为最后一个list的最后元素):lset <key> <index> <value>
                获取:
                    1.移除并返回key的第一个元素:lpop <key>
                    2.移除并返回key的最后一个元素:rpop <key>
                    3.返回指定下标间内元素列表:lrange <key> <start> <end>
                其他:
                    1.裁剪列表，返回原集合的子集:ltrim <key> <start> <stop>
                    2.返回列表长度:llen <key>
                    3.返回列表中索引对应的元素:lindex <key> <index>
            集合set:
                设置:
                    1.添加元素:sadd <key> <member> <member>...
                获取:
                    1.返回集合所有元素:smembers <key>
                    2.返回集合元素个数:scard <key>
                其他:
                    1.多个集合的交集:sinter <key> <key>...
                    2.某集合和其他集合的差集(key1的差集):sdiff <key1> <key2>...
                    3.多个集合的并集:sunion <key> <key>...
                    4.判断元素是否在集合中（1为有，0为无）:sismember <key> <member>
            有序集合zset(score的插入有先后顺序排列):
                设置:
                    1.添加:zadd <key> <score> <member> <score> <member>...
                获取:
                    1.返回指定（下标）范围的元素:zrange <key> <start> <stop>
                    2.返回元素个数:zcard <key>
                    3.返回有序集合key中，score的之间的成员:zcount <key> <min> <max>
                    4.返回有序集合key中，成员member的score值:zscore <key> <member>
            
            
            
"""




















