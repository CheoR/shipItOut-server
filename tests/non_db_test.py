from django.test import TestCase
import unittest

class TestNonDB(unittest.TestCase):
    def setUp(self):
        print("non db setup")
    
    def test_not_db_print(self):
        print("non test_db works")
