from exceptions.exception import NotFoundException


class Students:

    def __init__(self):
        self.students = []

    def add_student(self,student_name):
        student = {"name": student_name}
        self.students.append(student)
        return student

    def remove_student(self, student_name):
        for student in self.students:
            if student.name == student_name:
                self.students.remove(student)
                return

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

    def __repr__(self):
        return f"Students: {', '.join(self.students)}"
