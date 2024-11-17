from flask import Flask
from markupsafe import escape
from student import Student

app = Flask(__name__)
students = []

@app.route("/")
def students_list():
    formatted_list = ""
    for student in students:
        formatted_list += f"Student name: {student.name}, Student number: {student.id_number}<br>\n"
    return f"""
    <p>Hello, here are all students:</p>
    <p>{formatted_list}</p>
    """

@app.route('/add_student/<string:name>;<int:id_number>')
def add_student(name, id_number):
    new_student_name = escape(name)
    new_student_id = escape(id_number)
    new_student = Student(new_student_name, new_student_id)
    students.append(new_student)
    userdata = f'Student {new_student_name} with ID: {new_student_id} added in the list'
    return userdata

@app.route('/delete_student/<int:id_number>')
def delete_student(id_number):
    userdata = ""
    student_id = escape(id_number)
    for student in students:
        if student.id_number == student_id:
            students.remove(student)
            userdata = f'Student with ID: {student_id} removed from the list'
        else:
            userdata = f'Student with ID: {student_id} does not exist'
    return userdata


if __name__ == "__main__":
    app.run()

# URL examples:
# http://127.0.0.1:5000/
# http://127.0.0.1:5000/add_student/vasya;1
# http://127.0.0.1:5000/delete_student/1
