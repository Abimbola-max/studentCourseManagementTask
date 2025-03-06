from exceptions.exception import NotFoundException

class Students:

    def __init__(self):
        self.students = []

    def add_student(self, student_name):
        first_name, second_name = student_name
        self.students.append(student_name(first_name, second_name))

    def remove_student(self, student_name):
        for student in self.students:
            if student.name == student_name:
                self.students.remove(student)
                return True

        raise NotFoundException("Student not found")

    def number_of_students(self):
        return len(self.students)

    def find_student(self, student_name):
        for student in self.students:
            if student.name == student_name:
                return student

        raise NotFoundException("Student not found")

    def view_students(self):
        return [student.name for student in self.students]