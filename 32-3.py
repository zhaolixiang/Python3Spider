import pymysql

db=pymysql.connect(host='localhost',user='root',password='12345678',port=3306,db='spiders')
cursor=db.cursor()
sql='insert into students(id,name,age) values(%s,%s,%s)'
try:
    cursor.execute(sql,('1','mark','19'))
    db.commit()
except:
    print('出现错误了，进行回滚')
    db.rollback()
db.close()