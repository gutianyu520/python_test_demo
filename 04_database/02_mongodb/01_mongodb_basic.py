# -*- coding: utf-8 -*-
# @Time    : 2021/2/12 14:35
# @Author  : Lim Yoona
# @Site    : 
# @File    : 01_mongodb_basic.py
# @Software: PyCharm

"""mongodb"""
"""
    基本语法：
        查看当前数据库：db
        查看所有数据库：show dbs
        切换数据库：use <db>
        删除数据库: db.dropDatabase()
        
    创建集合
        db.createCollection(name,options)
            name:集合名称
            options:指定集合配置
        
        例1：不限制集合大小
            db.createCollection("stu")
        例2：限制集合大小
            db.createCollection("sub",{capped : true, size :10})
    
    查看集合
        show collections
    
    删除集合
        db.<collection>.drop()
        
    数据类型：
        ObjectID:文档ID
        string:字符串，最常用，必须是有效的utf-8
        boolean:true or false
        integer: 32或64位，取决于服务器
        double:浮点值
        arrays:数组或列表，多个值存储到一个key
        object:嵌入式文档，一个值为一个文档
        null:存储null值
        timestamp:时间戳
        date:存储当前日期或时间的unix时间格式
    
    object id:
        每个文档都有一个属性，为_id，保证每个文档的唯一性
        可以手动设置_id插入文档
        默认提供一个文档id，类型ObjectID
        objectID是一个12字节的十六进制数
            前4字节:当前时间戳
            后3字节:机器ID
            后2字节:服务进程id
            后3字节:增量值
         
    
    文档操作：
        插入:
            db.<collection>.insert(document)
                例1:
                    db.stu.insert({name:'gj',gender:1})
                例2:
                    s1={_id:'2020212',name:'hr'}
                    s1.gender=0
                    db.stu.insert(s1)
        简单查询:
            db.<collection>.find()
        更新：
            db.<collection>.update(
                <query>,
                <update>,
                {multi:<boolean>}
            )
                query:查询条件
                update:更新操作
                multi:可选，默认false，只更新一条，设置为true时则更新全部
            例1：全文档更新
                db.stu.update({name:'hr'},{name:'mnc'})
            例2：指定属性更新，通过操作符$set
                db.stu.update({name:'hr'},{$set:{name:'mnc'}})
            例3：修改多条匹配到的数据
                db.stu.update({},{$set:{gender:0}},{multi:true})
        
        保存：
            db.<collection>.save(document)
                文档id已存在则修改，不存在则添加
            例1:
                db.stu.save({_id:'20200212','name':'yk',gender:1})
            例2:
                db.stu.save({_id:'20160102','name':'wyk'})
        
        删除：
            db.<collection>.remove(
                <query>,
                {
                    justOne: <boolean>
                }
            )
                query:可选，删除条件
                justOne:可选，默认false，删除多条，设置true或1，表示只删除1条
            例1:按条件删除
                db.stu.remove({gender:0},{justOne:true})
            例2:全部删除
                db.stu.remove({})
    
    数据查询：
        基本查询：
            1.find()
                db.<collection>.find({条件})
            2.findOne()
                db.<collection>.findOne({条件})
            3.pretty():结果格式化
                db.<collection>.find({条件}).pretty()
        
        比较运算符：
            1.等于，默认，没有
            2.小于:$lt
            3.小于等于:$lte
            4.大于:$gt
            5.大于等于:$gte
            6.不等于:$ne
            例:
                db.stu.find({age:{$gte:18}})
        
        逻辑运算符：
            1.逻辑与
                db.<collection>.find(<条件1>,<条件2>...)
            2.逻辑或
                db.<collection>.find({$or:[<条件1>,<条件2>...]})
            3.逻辑与和逻辑或一起使用
                db.<collection>.find({$or:[<条件1>,<条件2>...]},<条件n>)
    
        范围运算符：
            $in,$nin
                db.stu.find({age:{$in:[10,18]}})
        
        正则表达式：
            //,$regex
                db.stu.find({name:/^黄/})
                db.stu.find({name:{$regex:'^黄'}})
        
        自定义查询：
            $where
                db.stu.find({$where:function(){return this.age>20}})
                
        limit:
            不填，默认所有
            db.<collection>.find().limit(NUMBER)
        
        skip:
            默认0
            db.<collection>.find().skip(NUMBER)
        
        limit和skip一起使用（limit和skip前后无所谓）
            db.stu.find().limit(4).skip(5)
        
        投影：
            db.<collection>.find({},{column:1,...})      
                1:表示显示
                0:表示不显示
                
        排序：
            db.<collection>.find().sort({column:1,...})
                1:升序
                -1:降序
        
        统计个数：
            db.<collection>.find({条件}).count()
            db.<collection>.count({条件})
                
        消除重复：
            db.<collection>.distinct('重复字段',{条件})
                例：
                    db.stu.distinct('gender',{age:{$gt:18}})
                
                
"""

# import pymongo
# client = pymongo.MongoClient('192.168.0.149', 27017)
# client.adb.authenticate("user_account", "account")
# db = client.account
# stu = db.stu
# s1 = {'name': 'gj', 'age': 18}
# s1_id = stu.insert_one(s1).inserted_id











