import pymysql


sql='select * from students where age>=1'
db=pymysql.connect(host='localhost',user='root',password='12345678',port=3306,db='spiders')

cursor=db.cursor()
cursor.execute(sql)
print('Count:',cursor.rowcount)

one=cursor.fetchone()
print('One:',one)

results=cursor.fetchall()
print('Results:',results)
print('Results Type:',type(results))
for row in results:
    print(row)


db.close()