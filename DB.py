#!/usr/bin/env python
# coding=utf-8

import pymysql
import hist
from collections import defaultdict
def connectdb():
    print('连接到mysql服务器...')
    # 打开数据库连接
    # 用户名:hp, 密码:Hp12345.,用户名和密码需要改成你自己的mysql用户名和密码，并且要创建数据库TESTDB，并在TESTDB数据库中创建好表Student
    db = pymysql.connect("120.77.148.34","root","zh123123" ,"ergouketang")
    print('连接上了!')
    return db

def createtable(db):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # 如果存在表Sutdent先删除
    cursor.execute("DROP TABLE IF EXISTS Student")
    sql = """CREATE TABLE Student (
            ID CHAR(10) NOT NULL,
            Name CHAR(8),
            Grade INT )"""

    # 创建Sutdent表
    cursor.execute(sql)

def query_ppt(db,userid):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql1="SELECT filename,page FROM ppt where user='{0}'".format(userid)
    # sql1="SELECT * FROM ppt"
    re=defaultdict(lambda :0)
    try:
        cursor.execute(sql1)
        temp=cursor.fetchall()
        fn=temp[-1][0]
        page=temp[-1][1]
        print(temp)
        print(fn)
        print(page)
        sql2="SELECT * FROM count where source='/counter/static/{0}.html'".format(fn)
        # sql2 = "SELECT key,count FROM count where source='/static/{0}.html'".format(fn)
        cursor.execute(sql2)
        results=cursor.fetchall()
        for row in results:
            re[int(row[2],16)]=row[3]
        return re,page,fn
    except:
        print("Error: unable to fecth data")


    # # SQL 查询语句
    # #sql = "SELECT * FROM Student \
    # #    WHERE Grade > '%d'" % (80)
    # sql2 = "SELECT * FROM count where source='/static/{0}.html'".format(filename)
    # try:
    #     # 执行SQL语句
    #     cursor.execute(sql)
    #     # 获取所有记录列表
    #     results = cursor.fetchall()
    #     for row in results:
    #         ID = row[0]
    #         Name = row[1]
    #         Grade = row[2]
    #         # 打印结果
    #         print "ID: %s, Name: %s, Grade: %d" % \
    #             (ID, Name, Grade)
    # except:
    #


def insertdb(db):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 插入语句
    sql = """INSERT INTO Student
         VALUES ('001', 'CZQ', 70),
                ('002', 'LHQ', 80),
                ('003', 'MQ', 90),
                ('004', 'WH', 80),
                ('005', 'HP', 70),
                ('006', 'YF', 66),
                ('007', 'TEST', 100)"""

    #sql = "INSERT INTO Student(ID, Name, Grade) \
    #    VALUES ('%s', '%s', '%d')" % \
    #    ('001', 'HP', 60)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # Rollback in case there is any error
        print('插入数据失败!')
        db.rollback()

def insert_user(db,uid):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 插入语句
    sql = "INSERT INTO user VALUES ('{0}',NULL,1)".format(uid)
    print(sql)
    #sql = "INSERT INTO Student(ID, Name, Grade) \
    #    VALUES ('%s', '%s', '%d')" % \
    #    ('001', 'HP', 60)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # Rollback in case there is any error
        print('插入数据失败!')
        db.rollback()

def check_binding(db,user):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    #sql = "SELECT * FROM Student \
    #    WHERE Grade > '%d'" % (80)
    sql = "SELECT isbinding FROM user where uid='{0}'".format(user)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            isbinding = row[0]

            # 打印结果
            print("isb: {0} " .format(isbinding))
                # (ID, Name, Grade)
        return isbinding
    except:
        print("Error: unable to fecth data")

def querydb(db):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    #sql = "SELECT * FROM Student \
    #    WHERE Grade > '%d'" % (80)
    sql = "SELECT * FROM Student"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            ID = row[0]
            Name = row[1]
            Grade = row[2]
            # 打印结果
            print("ID: %s, Name: %s, Grade: %d" % \
                (ID, Name, Grade))
    except:
        print("Error: unable to fecth data")

def deletedb(db):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 删除语句
    sql = "DELETE FROM Student WHERE Grade = '%d'" % (100)

    try:
       # 执行SQL语句
       cursor.execute(sql)
       # 提交修改
       db.commit()
    except:
        print('删除数据失败!')
        # 发生错误时回滚
        db.rollback()

def bind_courese(db,user,course):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 更新语句
    sql = "UPDATE user SET classid = '{0}',isbinding=0   WHERE uid = '{1}'".format (course,user)

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        print('更新数据失败!')
        # 发生错误时回滚
        db.rollback()

def updatedb(db):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 更新语句
    sql = "UPDATE Student SET Grade = Grade + 3 WHERE ID = '%s'" % ('003')

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        print('更新数据失败!')
        # 发生错误时回滚
        db.rollback()

def closedb(db):
    db.close()

def main():
    db = connectdb()    # 连接MySQL数据库

    # createtable(db)     # 创建表
    # insertdb(db)        # 插入数据
    # print '\n插入数据后:'
    # querydb(db)
    # deletedb(db)        # 删除数据
    # print '\n删除数据后:'
    # querydb(db)
    # updatedb(db)        # 更新数据
    # print '\n更新数据后:'
    # querydb(db)
    #
    re,len,fn=query_ppt(db,'o1bMd05yMLCudsJkhkdVxT2-3-lQ')
    hist.create_hist(len,re,fn)
    closedb(db)         # 关闭数据库

if __name__ == '__main__':
    main()