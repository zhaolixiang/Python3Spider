import pymysql


db=pymysql.connect(host='localhost',user='root',password='12345678',port=3306,db='spiders')
sql='Update students set age=%s where name=%s'
cursor=db.cursor()
try:
    if cursor.execute(sql,(25,'mark')):
        print('success')
        db.commit()
except:
    print('出现错误了，进行回滚')
    db.rollback()
db.close()