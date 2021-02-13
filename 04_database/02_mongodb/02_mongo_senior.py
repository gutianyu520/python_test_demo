# -*- coding: utf-8 -*-
# @Time    : 2021/2/12 17:51
# @Author  : Lim Yoona
# @Site    : 
# @File    : 02_mongo_senior.py
# @Software: PyCharm

"""mongodb高级操作"""

"""
    聚合：
        db.<collection>.aggregate([{管道:{表达式}}])
            常用管道：
                $group:将集合中的文档分组，可用于统计结果
                    1.集合文档分组，用于统计结果
                      _id:表示分组的依据，使用的字段用$标记
                      例：
                        db.stu.aggregate([{$group:{_id:'$gender',counter:{$sum:1}}}])
                    2.group by null:集合所有文档为一组
                      例:
                        db.stu.aggregate([{$group:{_id:null,counter:{$sum:1},avgAge:{$avg:'$age'}}}])
                    3.透视数据
                      例:
                        db.stu.aggregate([{$group:{_id:'$gender',name:{$push:'$name'}}}])
                        db.stu.aggregate([{$group:{_id:'$gender',name:{$push:'$$ROOT'}}}])
                $match:过滤数据，只输出符合条件的文档
                    1.用于过滤器，只输出符合条件的文档
                      例:
                        db.stu.aggregate([{$match:{age:{$gt:20}}}])
                        db.stu.aggregate([{$match:{age:{$gt:20}}},{$group:{_id:'$gender',counter:{$sum:1}}])
                $project:修改输入文档的结构，如重命名、增加、删除字段、创建计算结果
                    1.修改输入文档的结构，重命名、增加、删除字段、创建计算结果
                      例:
                        db.stu.aggregate([{$project:{_id:0,name:1,age:1}}])
                        db.stu.aggregate([{$group:{_id:'$gender',counter:{$sum:1}}},{$project:{_id:0,counter:1}}])
                $sort:将输入文档排序后输出
                    1.将输入文档排序后输出
                      例:
                        db.stu.aggregate([{$sort:{age:1}}])
                        db.stu.aggregate([{$group:{_id:'$gender',counter:{$sum:1}}},{$sort:{age:-1}}])
                $limit:限制聚合管道返回的文档数
                      例:
                        db.stu.aggregate([{$limit:2}])
                $skip:跳过指定数量的文档，并返回余下的文档(当skip和limit一起使用时，skip前，limit后)
                      例:
                        db.stu.aggregate([{$skip:2}])
                        db.stu.aggregate([{$group:{_id:'$gender',counter:{$sum:1}}},{$sort:{counter:1}},{$skip:1},{$skip:1}])
                $unwind:将数组类型的字段进行拆分
                    1.语法1
                        对字段进行拆分:db.<collection>.aggregate([{$unwind:'$<column>'}])
                    2.语法2
                        对字段进行拆分，处理空数组、非数组、无字段、null等情况:
                            db.<collection>.aggregate([{$unwind:{path:'$<column>',preserveNullAndEmptyArrays:<boolean>}}])
                            preserveNullAndEmptyArrays:防止数据丢失
            表达式：{表达式:'$列名'}
                $sum:计算总和
                $avg:计算平均值
                $min:获取最小值
                $max:获取最大值
                $push:在结果文档中插入值到一个数组中
                $first:获取第一个文档数据
                $last:获取最后一个文档数据
                
    超级管理员：
        为安全访问mongodb，需要创建用户密码
        安全管理方式:角色-用户-数据库
        常见系统角色:
            root:只在admin数据库可用，超级账号，超级权限
            read:允许用户读取指定数据库
            readwrite:允许用户读写指定数据库
        创建超级管理员:
            use admin
            db.createUser({user:'admin',pwd:'123',roles:[{role:'root',db:'admin'}]})
    
    启用安全认证:
        1.修改配置文件:sudo vi mongod.conf
        2.启用身份验证:
            security:
                authorization:enabled
        3.重启服务:
            sudo service mongod stop
            sudo service mongod start
        4.终端连接:mongo -u 'admin' -p '123' --authenticationDatabase 'admin'
    
    普通用户管理:
        1.使用超级管理员登录：use test1
        2.查看当前数据库的用户:show users
        3.创建普通用户:db.createUser({user:'t1',pwd:'123',roles:[{role:'readwrite',db:'test1'}]})
        4.终端连接:mongo -u 't1' -p '123' --authenticationDatabase 'test1'
        5.修改用户属性:db.updateUser('t1',{pwd:'456'})

    复制（副本集）
        定义：数据冗余备份，提高数据可用性，保证数据安全性，方便恢复数据
        作用：
            1.数据备份
            2.数据灾难恢复
            3.读写分离
            4.高数据可用性
            5.副本集对应用程序是透明的
        工作原理：
            1.复制至少需要两个节点（一主多副）
            2.主节点处理客户端请求
            3.副节点复制主节点上的数据
            4.搭配方式:一主一从，一主多从
            5.主副节点进行数据交互，保障数据一致性
        特点:
            1.n个节点的集群
            2.任何节点均可作为主节点
            3.所有写操作都在主节点上
            4.自动故障转移
            5.自动恢复
        设置复制节点:
            1.创建数据库目录:
                主:mkdir t1
                副:mkdir t2
            2.启动mongod:
                主:mongod --bind_ip 192.168.196.128 --port 27017 --dbpath ~/Desktop/t1 --replSet rs0
                副:mongod --bind_ip 192.168.196.128 --port 27018 --dbpath ~/Desktop/t2 --replSet rs0
            3.连接主节点:mongo --host 192.168.196.128 --port 27017
            4.主节点初始化:rs.initiate()
                初始化完成状态: rs0:SECONDARY>
            5.查看当前状态:rs.status()
            6.添加副本集:rs.add('192.168.196.128:27018')
            7.连接副节点:mongo --host 192.168.196.128 --port 27018
            8.主节点插入数据:
                use test1
                for(i=0;i<10;i++){db.t1.insert({_id:i})}
                db.t1.find()
            9.副节点进行查询操作:
                主:rs.slaveOk()
                副:db.t1.find()
            10.删除副节点:
                rs.remove(192.168.196.128:27018)
    
    备份:
        mongodump -h <dbhost:port> -d <dbname> -o <dbdirectory>
            -h:服务器地址，可用指定端口
            -d:需要备份的数据库名
            -o:备份数据的目录
    
    恢复:
        mongorestore -h <dbhost:port> -d <dbname> --dir <dbdirectory>
            -h:服务器地址，可用指定端口
            -d:需要恢复的数据库名
            -o:备份数据的目录
"""

import pymongo

"""创建客户端"""
client = pymongo.MongoClient('192.168.0.149', 27017)
"""获取数据库"""
db = client.test1
"""获得集合"""
stu = db.stu
"""添加文档"""
s1 = {'name': 'gj', 'age': 18}
s1_id = stu.insert_one(s1).inserted_id
"""查询一个文档"""
s2 = stu.find_one()
"""查询多个文档"""
s2 = stu.find()
"""获取文档数"""
count = stu.count()
