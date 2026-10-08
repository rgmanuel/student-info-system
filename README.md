# Student Information System

A simple Python-based Student Information System for managing student records. The system allows users to add, view, update, and delete student information. Student data is stored in a JSON file.

## Features

* Add student
* View all students
* View student by ID
* Update student information
* Delete student
* Basic input validation
* JSON data storage
* Error handling
* Activity logging
* Configuration file

## Technologies Used

* Python
* JSON
* Git
* GitHub
* Visual Studio Code

The project uses Python standard libraries, so no external packages are required.

## Project Structure

```text
student-info-system/
├── src/
│   ├── models/
│   │   ├── __init__.py
│   │   └── student.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── student_service.py
│   └── main.py
├── data/
│   └── students.json
├── config/
│   └── config.json
├── logs/
│   └── app.log
├── tests/
├── README.md
├── requirements.txt
└── .gitignore
```

## How to Run

1. Clone or download the repository.
2. Open the project folder in Visual Studio Code.
3. Open the terminal.
4. Run:

```text
python src/main.py
```

5. Choose an option from the menu.

## Git and GitHub

The project uses Git for version control and GitHub for repository hosting.

The `main` branch contains the main project, while the `feature/student-crud` branch was used to develop and improve the student CRUD functions.

## Author

Rg Gabriel G. Manuel
