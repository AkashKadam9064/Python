import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']
col = mydb["student"]

dick = {'1': 2049, '2': 4900, '5': 699}
x = col.insert_one(dick)

y = col.find_one()
print(y)

