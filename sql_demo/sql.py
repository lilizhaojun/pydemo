#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/23 10:17
# @Author  : lizhaojun
# @File    : sql.py
'''
连接数据库示例
'''
import pymysql
import traceback


def create_table():
    # 建立连接
    db = pymysql.connect(host='localhost', user='root', password='123789', db='mydb')
    # 使用cursor方法创建一个游标对象cursor
    cursor = db.cursor()

    # 创建数据库表
    cursor.execute('DROP TABLE IF EXISTS MYTABLE')

    sql = '''CREATE TABLE MYTABLE(
             FIRST_NAME CHAR(20) NOT NULL,
             LAST_NAME CHAR(20),
             AGE INT,
             SEX CHAR(1),
             INCOME FLOAT)
             '''
    cursor.execute(sql)

    # 插入数据
    sql2 = """INSERT INTO MYTABLE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
    sql3 = """INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)VALUES('xixi','haha',4,'M',855)"""
    try:
        cursor.execute(sql3)
        db.commit()
        print('写入数据')
    except:
        db.rollback()
        print('数据回滚')
        traceback.print_exc()

    db.close()


if __name__ == '__main__':
    create_table()
