from flask import Flask,jsonify, request
from flask_cors import CORS

app = Flask(__name__)

# @app.route('/')
# def hello():
#     return 'Flask is working'
# @app.route('/read')
# def hi():
#     return 'flask is not working'

CORS(app)
# @app.route('/<name>')
# def hi(name):
#     return f'Hello my name is {name}'
# if __name__ == '__main__':
#     app.run(debug=True)


# Dummy Data (list of dictionaries)
students = [
    {'id': 1, 'name': 'xyz', 'course': 'Python'},
    {'id': 2, 'name': 'abc', 'course': 'React'}
]

# GET – Read all data
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# POST – Add new student
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    students.append(data)
    return jsonify({"message": "Student added!"})

# PUT – Update student
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()
    for student in students:
        if student['id'] == id:
            student['name'] = data['name']
            student['age'] = data['age']
            return jsonify({"message": "Student updated!"})
    return jsonify({"message": "Student not found!"})

# DELETE – Remove student
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    for student in students:
        if student['id'] == id:
            students.remove(student)
            return jsonify({"message": "Student deleted!"})
    return jsonify({"message": "Student not found!"})

if __name__ == '__main__':
    app.run(debug=True)