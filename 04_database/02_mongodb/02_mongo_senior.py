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
                $match:过滤数据，只输出符合条件的文档
                $project:修改输入文档的结构，如重命名、增加、删除字段、创建计算结果
                $sort:将输入文档排序后输出
                $limit:限制聚合管道返回的文档数
                $skip:跳过指定数量的文档，并返回余下的文档
                $unwind:将数组类型的字段进行拆分
            表达式：{表达式:'$列名'}
                $sum:计算总和
                $avg:计算平均值
                $min:获取最小值
                $max:获取最大值
                $push:在结果文档中插入值到一个数组中
                $first:获取第一个文档数据
                $last:获取最后一个文档数据
                







"""

































