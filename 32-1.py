import pymysql

db=pymysql.connect(host='localhost',user='root',password='12345678',port=3306)
cursor=db.cursor()
cursor.execute('Select version()')
data=cursor.fetchone()
print('Datebase version:',data)

cursor.execute('create database spiders default character set utf8')
db.close()