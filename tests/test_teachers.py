import unittest

from exceptions.exception import NotFoundException
from src.teachers import Teachers


class MyTeachersTestCase(unittest.TestCase):

    def setUp(self):
        self.teacher_management = Teachers()

    def test_that_a_teacher_can_be_added(self):
        teacher = self.teacher_management.add_teacher("Dr Favour", "FavourIgwe@gamil.com")
        self.assertIn(teacher, self.teacher_management.teacher_list)
        self.assertEqual(teacher["name"], "Dr Favour")
        self.assertEqual(teacher["email"], "FavourIgwe@gamil.com")

    def test_that_a_teacher_can_be_removed(self):
        self.teacher_management.add_teacher("Dr Favour", "FavourIgwe@gamil.com")
        result = self.teacher_management.remove_teacher("FavourIgwe@gamil.com")
        self.assertTrue(result)
        with self.assertRaises(NotFoundException):
            self.teacher_management.remove_teacher("FavourIgwe@gamil.com")

    def test_find_teacher_by_email(self):
        self.teacher_management.add_teacher("Dr Favour", "FavourIgwe@gamil.com")
        teacher = self.teacher_management.find_teacher("FavourIgwe@gamil.com")
        self.assertIsNotNone(teacher)
        self.assertEqual(teacher["name"], "Dr Favour")
        self.assertEqual(teacher["email"], "FavourIgwe@gamil.com")

    def test_find_teacher_by_email_not_in_existence(self):
        with self.assertRaises(NotFoundException):
            self.teacher_management.find_teacher("Hamidd@gamil.com.com")
