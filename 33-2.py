import pymongo

client=pymongo.MongoClient(host='localhost',port=27017)
db=client.test

collection=db.students
students={
    'id':1,
    'name':'mark',
    'age':18
}


result=collection.insert_one(students)
print(result)
print(result.inserted_id)


students2={
    'id':2,
    'name':'face',
    'age':19
}

students3={
    'id':3,
    'name':'love',
    'age':20
}



result=collection.insert_many([students2,students3])
print(result)
print(result.inserted_ids)