from pymongo import MongoClient

def get_collection():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["pump_factory"]
    return db["alerts"]