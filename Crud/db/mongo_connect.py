from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
# "mongodb://localhost:27017/mydb/users"
db = client["mydb"]
collection = db["users"]
