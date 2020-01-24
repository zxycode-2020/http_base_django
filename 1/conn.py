# -*- coding: utf-8 -*-
import MySQLdb as db
try:
    conn = db.connect(user='root',passwd='1234',host='127.0.0.1',db='python',charset='utf8')
except Exception:
    print '连接异常'
print conn

cur = conn.cursor()

#sql = 'insert into user(name,pwd) values("八戒",222)'
#sql = 'delete from user where pwd=222'
#sql = 'update user set pwd="000"'
#sql = 'select * from user'rr

#sql = 'insert into user(name,pwd) values(%s,%s)'
#cur.execute(sql,('八戒','222'))
#cur.executemany(sql,[('八戒','222'),('沙僧','222')]) # 多条插入

#查询
sql = 'select * from user1'
print cur.execute(sql) # 返回记录条数，遍历方法如下
rose = cur.fetchall()
for id,name,pwd in rose:
    print id,name,pwd

conn.commit()
conn.close()