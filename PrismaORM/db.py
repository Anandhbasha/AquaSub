from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["Newone"]
collection = db["NewTable"]
