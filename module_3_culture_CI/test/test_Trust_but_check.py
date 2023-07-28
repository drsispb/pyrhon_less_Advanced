import datetime
from module_3_culture_CI.Trust_but_check import Person
from unittest import TestCase


from module_3_culture_CI.Trust_but_check import Person
class PersonTestCase(TestCase):
    def setUp(self):
        self.person = Person('Bob', 1976)
    def test_default_name_is_none(self):
        self.assertIsNotNone(self.person.name)
    def test_get_age(self):
        self.assertTrue(self.person.get_age() > 0)
        self.assertIsInstance(self.person.get_age(), int)

    def test_get_name(self):
         self.assertIsNotNone(self.person.name)

    def test_set_address(self):
        self.person.set_address('SPb')
        self.assertTrue(self.person.address, 'SPb')

    def test_get_address(self):
        self.person.set_address('SPb')
        self.assertTrue(self.person.get_address(), 'SPb')

    def test_is_homeless(self):
        self.person.set_address('')
        self.assertIsInstance(self.person.is_homeless(), bool)
