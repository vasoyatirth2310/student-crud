from models.student_model import Student, StudentCreate
from typing import Optional


# In-memory storage
students = []

# Automatically generate student IDs
next_id = 1


def create_student(student_data: StudentCreate) -> Student:
    global next_id

    student = Student(
        id=next_id,
        name=student_data.name,
        email=student_data.email,
        course=student_data.course,
        semester=student_data.semester
    )

    students.append(student)
    next_id += 1

    return student


def get_all_students():
    return students


def get_student_by_id(student_id: int) -> Optional[Student]:
    for student in students:
        if student.id == student_id:
            return student

    return None


def update_student(student_id: int, student_data: StudentCreate):
    for index, student in enumerate(students):
        if student.id == student_id:

            updated_student = Student(
                id=student_id,
                name=student_data.name,
                email=student_data.email,
                course=student_data.course,
                semester=student_data.semester
            )

            students[index] = updated_student

            return updated_student

    return None


def delete_student(student_id: int) -> bool:
    for index, student in enumerate(students):
        if student.id == student_id:
            students.pop(index)
            return True

    return False