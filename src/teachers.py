from exceptions.exception import NotFoundException

class Teachers:

    def __init__(self):
        self.teacher_list = []

    def add_teacher(self, teacher_name, teacher_email):
        teacher = {"name": teacher_name, "email": teacher_email}
        self.teacher_list.append(teacher)
        return teacher

    def remove_teacher(self, teacher_email: str) -> bool:
        for teacher in self.teacher_list:
            if teacher["email"] == teacher_email:
                self.teacher_list.remove(teacher)
                return True

        raise NotFoundException(f"Teacher with email {teacher_email} is not in the list.")

    def view_teachers(self):
        return self.teacher_list

    def get_number_of_teachers(self) -> int:
        return len(self.teacher_list)

    def find_teacher(self, teacher_email):
        for teacher in self.teacher_list:
            if teacher["email"] == teacher_email:
                return teacher

        raise NotFoundException(f"{teacher_email} is not registered.")

    def __repr__(self):
        return f"Teachers: {', '.join(self.teacher_list)}"
