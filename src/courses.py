from exceptions.exception import NotFoundException


class Courses:

    def __init__(self):
        self.__courses = []

    @property
    def courses(self):
        return self.__courses

    def add_course(self, course_code):
        if course_code not in self.__courses:
            self.__courses.append(course_code)

    def view_courses(self):
        for course in self.__courses:
            return course

    def delete_course(self, course):
        if course not in self.__courses:
            raise NotFoundException("Course not found")
        self.__courses.remove(course)

    def number_of_courses(self):
        return len(self.__courses)

    def find_course(self, course_code: str):
        for course in self.__courses:
            if course == course_code:
                return course

        raise NotFoundException("Course not found")