import unittest

from exceptions.exception import InvalidCourseCodeException, InvalidCourseTitleException, \
    StudentAlreadyEnrolledException, NullException
from src.course import Course


class MyCourseTestCase(unittest.TestCase):

    def test_that_course_can_be_created(self):
        course = Course("ENG201", "English")
        self.assertEqual(course.course_code, "ENG201")
        self.assertEqual(course.title, "English")

    def test_that_course_code_as_string_raises_invalid_course_code_exception(self):
        with self.assertRaises(InvalidCourseCodeException):
            course = Course("@@@@", "English")

    def test_that_course_title_as_int_raises_invalid_course_title_exception(self):
        with self.assertRaises(InvalidCourseTitleException):
            course = Course("201", 364457)

    def test_that_invalid_course_code_length_exception(self):
        with self.assertRaises(InvalidCourseCodeException):
            course = Course("89205161", "English")

    def test_that_empty_course_code_raises_null_exception(self):
        with self.assertRaises(NullException):
            course = Course("", "English")

    def test_that_empty_course_title_raises_null_exception(self):
        with self.assertRaises(NullException):
            course = Course("201", "")

    def test_that_grade_can_be_added_to_course(self):
        self.course = Course("ENG201", "English")
        self.course.add_grade("Ayo", 75)
        self.assertEqual(self.course.get_grade("Ayo"), 75)