# -*- coding: utf-8 -*-
# @Time    : 2021/2/12 13:49
# @Author  : Lim Yoona
# @Site    : 
# @File    : 04_mysql_encapsulation.py
# @Software: PyCharm

"""mysql封装"""

import pymysql


class MysqlHelper:
    def __init__(self, host, port, db, user, pwd, charset='utf-8'):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.pwd = pwd
        self.charset = charset

    def connect(self):
        self.conn = pymysql.connect(host=self.host, port=self.port, db=self.db,
                                    user=self.user, password=self.pwd, charset=self.charset)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def get_one(self, sql, params=()):
        result = None
        try:
            self.connect()
            self.cursor.execute(sql,params)
            result = self.cursor.fetchone()
        except Exception as e:
            print(e.__doc__)
        return result

    def get_all(self, sql, params=()):
        list = ()
        try:
            self.connect()
            self.cursor.execute(sql, params)
            list = self.cursor.fetchall()
        except Exception as e:
            print(e.__doc__)
        return list

    def insert(self, sql, params=()):
        return self._edit(sql, params)

    def update(self, sql, params=()):
        return self._edit(sql, params)

    def delete(self, sql, params=()):
        return self._edit(sql, params)

    def _edit(self, sql, params=()):
        count = 0
        try:
            self.connect()
            count = self.cursor.execute(sql, params)
            self.conn.commit()
        except Exception as e:
            print(e.__doc__)
        finally:
            self.close()
        return count














