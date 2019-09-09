import pymysql

data={
    'id':'2',
    'name':'face',
    'age':19
}
table='students'
keys=','.join(data.keys())
values=','.join(['%s']*len(data))
sql='insert into {table}({keys}) values ({values})'.format(table=table,
                                                             keys=keys,
                                                             values=values)
db=pymysql.connect(host='localhost',user='root',password='12345678',port=3306,db='spiders')
cursor=db.cursor()
try:
    if  cursor.execute(sql,tuple(data.values())):
        print('success')
        db.commit()
except:
    print('出现错误了，进行回滚')
    db.rollback()
db.close()