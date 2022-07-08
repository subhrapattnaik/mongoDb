# mongoDb

MongoDB stores data in JSON-like documents, which makes the database very flexible and scalable.
NoSQL database is MongoDB.

You can download a free MongoDB database at https://www.mongodb.com.
---------------------------------------------------------------------------------
PyMongo
Python needs a MongoDB driver to access the MongoDB database.

 we will use the MongoDB driver "PyMongo".

We recommend that you use PIP to install "PyMongo".

pip3 install PyMongo
---------------------------------------------------------------------------------

To test if the installation was successful, or if you already have "pymongo" installed, create a Python page with the following content:

import pymongo
----------------------------------

To create a database in MongoDB, start by creating a MongoClient object, then specify a connection URL with the correct ip address and the name of the database you want to create.

MongoDB will create the database if it does not exist, and make a connection to it.
*******************************************************************************************************
Important: In MongoDB, a database is not created until it gets content!

Remember: In MongoDB, a database is not created until it gets content, so if this is your first time creating a database, you should complete the next two chapters (create collection and create document) before you check if the database exists!

Important: In MongoDB, a collection is not created until it gets content!

MongoDB waits until you have inserted a document before it actually creates the collection.
***********************************************************************************************************
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]


*************
You can check if a database exist by listing all databases in you system:

print(myclient.list_database_names())

  ================================================================================================================
  
  To create a collection in MongoDB, use database object and specify the name of the collection you want to create.

MongoDB will create the collection if it does not exist.
*************
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

mycol = mydb["customers"]
**************

  Return a list of all collections in your database:

print(mydb.list_collection_names())
=================================================================================================================
Insert Into Collection
To insert a record, or document as it is called in MongoDB, into a collection, we use the insert_one() method.

The first parameter of the insert_one() method is a dictionary containing the name(s) and value(s) of each field in the document you want to insert.

------------
To insert multiple documents into a collection in MongoDB, we use the insert_many() method.

The first parameter of the insert_many() method is a list containing dictionaries with the data you want to insert:

---------------
In MongoDB we use the find and findOne methods to find data in a collection.

Just like the SELECT statement is used to find data in a table in a MySQL database.
To select data from a collection in MongoDB, we can use the find_one() method.

The find_one() method returns the first occurrence in the selection.

The find() method returns all occurrences in the selection.



