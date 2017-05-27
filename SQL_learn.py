# encoding="utf-8"
#! /usr/bin/python

import pymssql

conn = pymssql.connect(server='127.0.0.1', user='sa', password='a68503060', database="HelloWorld", charset='UTF-8')
cursor = conn.cursor()
cursor.execute("select * from 总经办")
# 筛选出一个
# print(cursor.fetchone())
# 筛选出全部
print(cursor.fetchall())

# INSERT
# cursor.execute("INSERT INTO 总经办(id) VALUES (%s) ", 30)
# DELETE
# cursor.execute("DELETE FROM 总经办  WHERE 申请项目 IS NULL ")
# 最后关闭
conn.commit()



