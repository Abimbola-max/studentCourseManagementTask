import unittest

from src.Teachers import Teachers


class MyTeachersTestCase(unittest.TestCase):

    def setUp(self):
        self.teachers_management = Teachers()

    def test_that_a_teacher_can_be_added(self):
        name = self.teachers_management.add_teacher("Dr Ayo")
        self.assertIn(name, self.teachers_management.view_teachers())

