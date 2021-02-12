# -*- coding: utf-8 -*-
# @Time    : 2021/2/12 12:00
# @Author  : Lim Yoona
# @Site    : 
# @File    : 01_mysql_create.py
# @Software: PyCharm

"""mysql的导入和表的创建"""


from pymysql import connect

db = connect(host='192.168.0.161', user='root', password='root1234%', db='test', port=3306,charset='utf8mb4')
cur = db.cursor()
sql = """
    CREATE TABLE user(
        id int(11) auto_increment primary key not null ,
        name char(20) not null default '',
        password int(12),
        age int(3)
    )
"""
cur.execute(sql)
print("create table ok")
db.close()
"""
    cursor()方法创建数据库游标。
    execute()方法执行SQL语句。
    commit()将数据库的操作真正的提交到数据。
"""
























