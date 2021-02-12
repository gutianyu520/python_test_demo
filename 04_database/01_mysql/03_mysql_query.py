# -*- coding: utf-8 -*-
# @Time    : 2021/2/12 13:33
# @Author  : Lim Yoona
# @Site    : 
# @File    : 03_mysql_query.py
# @Software: PyCharm

"""mysql查询数据"""

from pymysql import connect

db = connect(user='root',host='192.168.0.161',password='root1234%',db='test')
cur = db.cursor()
try:
    """查询单条记录"""
    # sql = 'select * from user where id = 2'
    # cur.execute(sql)
    # result = cur.fetchone()
    """查询多条记录"""
    sql = 'select * from user'
    cur.execute(sql)
    result = cur.fetchall()
    print(result)
except Exception as e:
    print(e.__doc__)
finally:
    cur.close()
    db.close()































