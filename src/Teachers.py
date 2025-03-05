from exceptions.exception import NotFoundException
from src.teacher import Teacher


class Teachers:

    def __init__(self):
        self.teacher_list = []

    def add_teacher(self, teacher_name):
        teacher = {"name": teacher_name}
        self.teacher_list.append(teacher)
        return teacher

    def remove_teacher(self, teacher_name: str) -> bool:
        for teacher in self.teacher_list:
            if teacher["name"] == teacher_name:
                self.teacher_list.remove(teacher)
                return True
        raise NotFoundException(f"{teacher_name} is not in the list.")


    def view_teachers(self):
        return self.teacher_list

    def find_teacher(self, teacher_name) -> Teacher:
        for teacher in self.teacher_list:
            if teacher["name"] == teacher_name:
                return teacher

        raise NotFoundException(f"{teacher_name} is not in the list.")

    def total_teachers(self) -> int:
        return len(self.teacher_list)

    def __repr__(self):
        return f"Teachers: {', '.join(self.teacher_list)}"
