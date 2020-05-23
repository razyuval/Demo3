import pymongo

myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
mydict = {"name": "Yuval", "Age": "to old"}
# x= mycol.insert_one(mydict)
for x in mycol.find({},{"_id":0}):
    print(x)
# print (myclient.list_database_names()):

mylist = [
{'name':'Efi','Address':'Haornim 42'},
{'name':'Liad','Address':'Haornim 43'},
{'name':'Yuval','Address':'shvil kislev 23'},
{'name':'Ella','BlaBla':'kdksms'},
{'name':'Barucv','POBox':'37611'},
{'name':'Cruvi','Age':'34'},
{'name':'Arik','Bike':'Honda'},
{'name':'Bentz','Bike':'Ducati'},
]

x=  mycol.insert_many(mylist)
print(x.inserted_ids)

