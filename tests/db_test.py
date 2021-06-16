from django.test import TestCase
import unittest

class TestDB(unittest.TestCase):
    def setUp(self):
        print("test_db setup")
    
    def test_db_print(self):
        print("test_db works")
