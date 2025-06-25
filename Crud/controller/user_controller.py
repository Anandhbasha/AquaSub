import json
from bson import ObjectId
from db.mongo_connect import collection

def get_all_users():
    users = list(collection.find())
    for user in users:
        user["_id"] = str(user["_id"])
    return json.dumps(users)

def add_user(data):
    result = collection.insert_one(data)
    return json.dumps({"inserted_id": str(result.inserted_id)})

def update_user(user_id, data):
    result = collection.update_one({"_id": ObjectId(user_id)}, {"$set": data})
    return json.dumps({"updated_count": result.modified_count})

def delete_user(user_id):
    result = collection.delete_one({"_id": ObjectId(user_id)})
    return json.dumps({"deleted_count": result.deleted_count})
