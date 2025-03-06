import unittest

from exceptions.exception import NotFoundException
from src.courses import Courses


class MyCourseTestCase(unittest.TestCase):

    def setUp(self):
        self.courses = Courses()

    def test_that_courses_can_be_added(self):
        self.courses.add_course("MATH102")
        self.assertIn("MATH102", self.courses.courses)
        self.courses.add_course("MATH202")
        self.assertIn("MATH202", self.courses.courses)
        self.assertEqual(2, self.courses.number_of_courses())

    def test_that_courses_can_be_removed(self):
        self.courses.add_course("MATH102")
        self.assertIn("MATH102", self.courses.courses)
        self.courses.add_course("MATH202")
        self.assertIn("MATH202", self.courses.courses)
        self.assertEqual(2, self.courses.number_of_courses())

        self.courses.delete_course("MATH102")
        self.assertNotIn("MATH102", self.courses.courses)
        self.assertEqual(1, self.courses.number_of_courses())

    def test_for_non_course_existence_throws_not_found_exception_and_cannot_be_deleted(self):
        with self.assertRaises(NotFoundException):
            self.courses.delete_course("MATH345")

    def test_that_course_can_be_found(self):
        self.courses.add_course("MATH102")
        self.assertIn("MATH102", self.courses.courses)

        self.courses.add_course("MATH202")
        self.assertIn("MATH202", self.courses.courses)

        self.assertEqual(2, self.courses.number_of_courses())

        find = self.courses.find_course("MATH102")
        find_second = self.courses.find_course("MATH202")

        self.assertEqual("MATH102", find)
        self.assertEqual("MATH202", find_second)

    def test_for_non_course_existence_throws_not_found_exception(self):
        self.courses.add_course("MATH102")
        self.assertIn("MATH102", self.courses.courses)
        with self.assertRaises(NotFoundException):
            self.courses.find_course("MATH202")




