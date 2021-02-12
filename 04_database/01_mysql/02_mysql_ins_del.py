# -*- coding: utf-8 -*-
# @Time    : 2021/2/12 12:26
# @Author  : Lim Yoona
# @Site    : 
# @File    : 02_mysql_ins_del.py
# @Software: PyCharm

"""MySQL数据的插入和删除"""

from pymysql import connect
db = connect(host='192.168.0.161', user='root', password='root1234%', db='test', port=3306)
cur = db.cursor()
try:
    """新增"""
    # sql = """insert into user values(null,'xiaming',123456,20)"""
    """修改"""
    # sql = """update user set password = '654321' where name = 'xiaming'"""
    """删除"""
    # sql = """delete from user where id = 1"""
    """SQL语句参数化"""
    name = input('please input username:')
    param = [name]
    sql = """insert into user values (null,%s,123456,20)"""
    count = cur.execute(sql, param)
    print('insert counts : ', count)
except Exception as e:
    print(e.__doc__)
finally:
    db.commit()
    cur.close()
    db.close()



