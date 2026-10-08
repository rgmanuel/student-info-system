import logging
import json

from services.student_service import StudentService


# Load configuration
try:
    with open("config/config.json", "r") as file:
        config = json.load(file)
except FileNotFoundError:
    config = {
        "data_file": "data/students.json",
        "log_file": "logs/app.log"
    }


# Logging setup
logging.basicConfig(
    filename=config["log_file"],
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


class StudentInformationSystem:

    def __init__(self):
        self.student_service = StudentService(config["data_file"])

    def display_menu(self):
        print("\n==============================")
        print("   STUDENT INFORMATION SYSTEM")
        print("==============================")
        print("1. Add Student")
        print("2. View All Students")
        print("3. View Student by ID")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        print("==============================")

    def add_student(self):
        print("\n--- Add New Student ---")

        name = input("Name: ")
        email = input("Email: ")
        course = input("Course: ")
        year_level = input("Year Level: ")

        if not name or not email or not course or not year_level:
            print("Please fill in all fields.")
            return

        student_data = {
            "name": name,
            "email": email,
            "course": course,
            "year_level": year_level
        }

        try:
            student = self.student_service.add_student(student_data)

            logger.info("Added student: %s", student["student_id"])

            print("\nStudent added successfully!")
            print("Student ID:", student["student_id"])

        except Exception as e:
            logger.error("Error adding student: %s", e)
            print("Something went wrong while adding the student.")

    def view_all_students(self):
        print("\n--- All Students ---")

        students = self.student_service.get_all_students()

        if not students:
            print("No students found.")
            return

        for student in students:
            print("------------------------------")
            print("ID:", student["student_id"])
            print("Name:", student["name"])
            print("Email:", student["email"])
            print("Course:", student["course"])
            print("Year Level:", student["year_level"])

    def view_student(self):
        print("\n--- View Student ---")

        student_id = input("Enter Student ID: ")

        student = self.student_service.get_student(student_id)

        if student:
            print("\nStudent Details")
            print("------------------------------")
            print("ID:", student["student_id"])
            print("Name:", student["name"])
            print("Email:", student["email"])
            print("Course:", student["course"])
            print("Year Level:", student["year_level"])
        else:
            print("Student not found.")

    def update_student(self):
        print("\n--- Update Student ---")

        student_id = input("Enter Student ID: ")

        student = self.student_service.get_student(student_id)

        if not student:
            print("Student not found.")
            return

        print("Press Enter if you want to keep the old value.")

        name = input(f"Name ({student['name']}): ")
        email = input(f"Email ({student['email']}): ")
        course = input(f"Course ({student['course']}): ")
        year_level = input(f"Year Level ({student['year_level']}): ")

        update_data = {
            "name": name if name else student["name"],
            "email": email if email else student["email"],
            "course": course if course else student["course"],
            "year_level": year_level if year_level else student["year_level"]
        }

        updated = self.student_service.update_student(
            student_id,
            update_data
        )

        if updated:
            logger.info("Updated student: %s", student_id)
            print("Student updated successfully.")
        else:
            print("Unable to update student.")

    def delete_student(self):
        print("\n--- Delete Student ---")

        student_id = input("Enter Student ID: ")

        student = self.student_service.get_student(student_id)

        if not student:
            print("Student not found.")
            return

        print("Student:", student["name"])

        confirm = input("Are you sure you want to delete this student? (y/n): ")

        if confirm.lower() == "y":
            deleted = self.student_service.delete_student(student_id)

            if deleted:
                logger.info("Deleted student: %s", student_id)
                print("Student deleted successfully.")
        else:
            print("Delete cancelled.")

    def run(self):
        while True:
            self.display_menu()

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.view_all_students()

            elif choice == "3":
                self.view_student()

            elif choice == "4":
                self.update_student()

            elif choice == "5":
                self.delete_student()

            elif choice == "6":
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    app = StudentInformationSystem()
    app.run()