#Delete the document with the address "Mountain 21":
#To delete one document, we use the delete_one() method.

#The first parameter of the delete_one() method is a query object defining which document to delete.


import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": "Mountain 21" }

mycol.delete_one(myquery)