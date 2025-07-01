def serialize_student(student):
    return {
        "id": str(student.get("_id")),
        "name": student.get("name", ""),   
        "email": student.get("email", "") 
    }
