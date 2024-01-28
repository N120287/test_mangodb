import pymongo
client = pymongo.MongoClient("mongodb+srv://shaikrajak0087:Rajak123@cluster0.qapsjlf.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"Rajak",
    "email" : "shaikrajak0087@gmail.com",
    "surname" : "shaik"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)