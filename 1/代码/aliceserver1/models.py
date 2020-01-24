# -*- coding: utf-8 -*-
import MySQLdb as db # 起别名db
try:
    conn = db.connect(user='root',passwd='root',host='127.0.0.1',db='1701demo',charset='utf8') #连接数据库
except Exception as e:
    print str(e)
    print '连接异常'

cur = conn.cursor()
# sql = 'insert into `1701`(name) VALUES("陈秋雨")'
# res = cur.execute(sql) # 返回影响行数
sql = 'select * from `1701`'
cur.execute(sql)
rose = cur.fetchall()
for item in rose:
    print item[0],item[1]
conn.commit() # 提交

conn.close() #关闭连接