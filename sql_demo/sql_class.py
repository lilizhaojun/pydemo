#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/27 10:44
# @Author  : lizhaojun
# @File    : sql_class.py
import traceback
import pymysql


class PyToMysql:
    def __init__(self):
        # 建立连接
        self.db = pymysql.connect(host='localhost', user='root', password='123789', db='mydb')
        # 使用cursor方法创建一个游标对象cursor
        self.cursor = self.db.cursor()

    def create_table(self):
        # 创建数据库表
        self.cursor.execute('DROP TABLE IF EXISTS MYTABLE')

        sql = '''CREATE TABLE MYTABLE(
                     FIRST_NAME CHAR(20) NOT NULL,
                     LAST_NAME CHAR(20),
                     AGE INT,
                     SEX CHAR(1),
                     INCOME FLOAT)
                     '''
        self.cursor.execute(sql)

    def close(self):
        #关闭数据库
        self.db.close()

    def exe(self,sql):
        #执行语句
        try:
            self.cursor.execute(sql)
            self.db.commit()
            print("执行完毕")
        except Exception as e:
            self.db.rollback()
            print("数据回滚" + e)

    def insert_data(self,data):
        # 插入数据
        sql2 = """INSERT INTO MYTABLE(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME)
                                      VALUES 
                                      ('%s','%s','%d','%s','%d')""" % (data[0],data[1],int(data[2]),data[3],int(data[4]))
        try:
            self.cursor.execute(sql2)
            self.db.commit()
            print('写入数据')
        except Exception as e:
            self.db.rollback()
            print('数据回滚' + e)
            traceback.print_exc()

    def find_data(self,money):
        # 数据库查询操作
        sql4 = "SELECT * FROM EMPLOYEE WHERE INCOME > '%d'" % (money)
        try:
            self.cursor.execute(sql4)
            result = self.cursor.fetchall()
            for row in result:
                print("fname = %s,lname = %s,age = %d,sex = %s,income = %d" % (row[0], row[1], row[2], row[3], row[4]))
        except Exception as e:
            print("Error:unable to fetch data" + e)

    def update_data(self):
        #数据更新
        sql5 = "update employee set age = age + 1 "
        try:
            self.cursor.execute(sql5)
            self.db.commit()
            print("更新完成")
        except Exception as e:
            self.db.rollback()
            print("数据回滚" + e)

    def delect_data(self):
        #数据删除
        sql6 = "delete from employee where first_name = '%s'" % ('fname')
        self.exe(sql6)


if __name__ == '__main__':
    pyToMysql = PyToMysql()
    #pyToMysql.find_data(3000)
    #写入数据
    #data = input('请分别输入：FIRST_NAME,LAST_NAME,AGE,SEX,INCOME,以逗号隔开')
    #data = data.split(',')
    #pyToMysql.insert_data(data)

    #更新数据
    #pyToMysql.update_data()

    #删除数据
    pyToMysql.delect_data()


    pyToMysql.close()


