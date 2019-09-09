import pymysql


sql='select * from students where age>=1'
db=pymysql.connect(host='localhost',user='root',password='12345678',port=3306,db='spiders')

cursor=db.cursor()
cursor.execute(sql)

row=cursor.fetchone()
while row:
    print('Row:',row)
    row=cursor.fetchone()


db.close()