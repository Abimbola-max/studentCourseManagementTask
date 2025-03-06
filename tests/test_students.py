import unittest

from exceptions.exception import NotFoundException
from src.students import Students


class MyStudentsTestCase(unittest.TestCase):

    def setUp(self):
        self.students_management = Students()

