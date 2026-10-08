import json
import os
from datetime import datetime

from models.student import Student


class StudentService:

    def __init__(self, data_file="data/students.json"):
        self.data_file = data_file
        self.create_data_file()

    def create_data_file(self):
        folder = os.path.dirname(self.data_file)

        if folder:
            os.makedirs(folder, exist_ok=True)

        if not os.path.exists(self.data_file):
            with open(self.data_file, "w") as file:
                json.dump([], file)

    def load_students(self):
        try:
            with open(self.data_file, "r") as file:
                return json.load(file)

        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_students(self, students):
        with open(self.data_file, "w") as file:
            json.dump(students, file, indent=4)

    # CREATE
    def add_student(self, student_data):
        students = self.load_students()

        student = Student(
            student_data["name"],
            student_data["email"],
            student_data["course"],
            student_data["year_level"]
        )

        students.append(student.to_dict())
        self.save_students(students)

        return student.to_dict()

    # READ
    def get_all_students(self):
        return self.load_students()

    def get_student(self, student_id):
        students = self.load_students()

        for student in students:
            if student["student_id"] == student_id:
                return student

        return None

    # UPDATE
    def update_student(self, student_id, update_data):
        students = self.load_students()

        for student in students:
            if student["student_id"] == student_id:

                student["name"] = update_data["name"]
                student["email"] = update_data["email"]
                student["course"] = update_data["course"]
                student["year_level"] = update_data["year_level"]
                student["updated_at"] = datetime.now().isoformat()

                self.save_students(students)

                return student

        return None

    # DELETE
    def delete_student(self, student_id):
        students = self.load_students()

        new_students = [
            student for student in students
            if student["student_id"] != student_id
        ]

        if len(new_students) == len(students):
            return False

        self.save_students(new_students)

        return True