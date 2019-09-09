import pymongo
from bson.objectid import ObjectId

client=pymongo.MongoClient(host='localhost',port=27017)
db=client.test

collection=db.students

result=collection.find_one({'name':'mark'})
print(type(result))
print(result)

result=collection.find_one({'_id':ObjectId('5d71067f3fddc800cc9222e6')})
print(result)

results=collection.find({'name':'mark'})
print(results)
for result in results:
    print(result)

print('*'*30)

results=collection.find({'age':{'$gt':18}})
for result in results:
    print(result)

print('-'*30)

results=collection.find({'name':{'$regex':'^m.*'}})
for result in results:
    print(result)

print('*'*30)
count=collection.find().count()
print(count)

count=collection.find({'age':18}).count()
print(count)

print('*'*30)

results=collection.find().sort('name',pymongo.ASCENDING)
print([result['name'] for result in results])

results=collection.find().sort('name',pymongo.ASCENDING).skip(2)
print([result['name'] for result in results])

results=collection.find().sort('name',pymongo.ASCENDING).skip(2).limit(2)
print([result['name'] for result in results])

# 更新
print('更新')
condition={'name':'mark'}
student=collection.find_one(condition)
print(student)
student['age']=25
result=collection.update(condition,student)
print(result)

result=collection.update_one(condition,{'$set':student})
print(result)
print(result.matched_count,result.modified_count)

condition={'age':{'$gt':24}}
result=collection.update_one(condition,{'$inc':{'age':1}})
print(result)
print(result.matched_count,result.modified_count)


condition={'age':{'$gt':19}}
result=collection.update_many(condition,{'$inc':{'age':1}})
print(result)
print(result.matched_count,result.modified_count)


result=collection.remove({'name':'mark'})
print(result)