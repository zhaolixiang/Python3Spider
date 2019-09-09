import pymysql

data={
    'id':'1',
    'name':'mark',
    'age':20
}
table='students'
key=','.join(data.keys())
values=','.join(['%s']*len(data))
sql='insert into {table}({key}) values ({values}) on duplicate key update'.format(
    table=table,
    key=key,
    values=values
)
update=','.join([" {key}=%s".format(key=key) for key in data])
sql+=update
print(sql)
db=pymysql.connect(host='localhost',user='root',password='12345678',port=3306,db='spiders')


cursor=db.cursor()
try:
    if cursor.execute(sql,tuple(data.values())*2):
        print('success')
        db.commit()
except:
    print('出现错误了，进行回滚')
    db.rollback()
db.close()