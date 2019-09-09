import pymongo

client=pymongo.MongoClient(host='localhost',port=27017)
db=client.test

collection=db.students
students={
    'id':1,
    'name':'mark',
    'age':18
}

result=collection.insert(students)
print(result)



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

result=collection.insert([students2,students3])
print(result)


