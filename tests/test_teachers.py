import unittest

from src.Teachers import Teachers


class MyTeachersTestCase(unittest.TestCase):

    def setUp(self):
        self.teachers_management = Teachers()

    def test_that_a_teacher_can_be_added(self):
        name = self.teachers_management.add_teacher("Dr Ayo")
        self.assertIn(name, self.teachers_management.view_teachers())

    def test_that_a_teacher_can_be_removed(self):
        name = self.teachers_management.add_teacher("Dr Ayo")
        second_name = self.teachers_management.add_teacher("Dr Favour")
        self.assertIn(name, self.teachers_management.view_teachers())
        self.assertIn(second_name, self.teachers_management.view_teachers())
        self.teachers_management.remove_teacher("Dr Favour")
        self.assertNotIn(second_name, self.teachers_management.view_teachers())
        self.assertTrue(second_name not in self.teachers_management.view_teachers())

