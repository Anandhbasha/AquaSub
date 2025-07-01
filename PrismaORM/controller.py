from flask import jsonify, request
from bson import ObjectId
from db import collection
from models import serialize_student

# CREATE
def create_student():
    data = request.json
    result = collection.insert_one({
        "name": data["name"],
        "email": data["email"]
    })
    return jsonify({"message": "Student created", "id": str(result.inserted_id)})

def get_students():
    students = collection.find()
    return jsonify([serialize_student(s) for s in students])

def get_student(student_id):
    student = collection.find_one({"_id": ObjectId(student_id)})
    if student:
        return jsonify(serialize_student(student))
    else:
        return jsonify({"error": "Student not found"}), 404

def update_student(student_id):
    data = request.json
    result = collection.update_one(
        {"_id": ObjectId(student_id)},
        {"$set": {
            "name": data["name"],
            "email": data["email"]
        }}
    )
    if result.matched_count:
        return jsonify({"message": "Student updated"})
    return jsonify({"error": "Student not found"}), 404

def delete_student(student_id):
    result = collection.delete_one({"_id": ObjectId(student_id)})
    if result.deleted_count:
        return jsonify({"message": "Student deleted"})
    return jsonify({"error": "Student not found"}), 404
