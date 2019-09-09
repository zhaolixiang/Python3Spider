import pymysql

table='students'
condition='age>19'
sql='delete from {table} where {condition}'.format(
    table=table,
    condition=condition
)
db=pymysql.connect(host='localhost',user='root',password='12345678',port=3306,db='spiders')

cursor=db.cursor()
try:
    if cursor.execute(sql):
        print('success')
        db.commit()
except:
    print('出现错误了，进行回滚')
    db.rollback()
db.close()