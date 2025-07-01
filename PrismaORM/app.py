from flask import Flask
from controller import (
    create_student, get_students,
    get_student, update_student, delete_student
)


app = Flask(__name__)

app.add_url_rule("/students", "create_student", create_student, methods=["POST"])
app.add_url_rule("/students", "get_students", get_students, methods=["GET"])
app.add_url_rule("/students/<student_id>", "get_student", get_student, methods=["GET"])
app.add_url_rule("/students/<student_id>", "update_student", update_student, methods=["PUT"])
app.add_url_rule("/students/<student_id>", "delete_student", delete_student, methods=["DELETE"])

if __name__ == "__main__":
    print(app.url_map) 
    app.run(debug=True)