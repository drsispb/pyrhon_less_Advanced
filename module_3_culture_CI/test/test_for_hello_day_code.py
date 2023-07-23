'''Задача 1. Хорошего дня!'''
import unittest
from datetime import datetime
from module_3_culture_CI.hello_day_code import app

from freezegun import freeze_time


class TestWeekdate(unittest.TestCase):

    def setUp(self) -> None:
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello/'

    def test_get_username(self):
        username = 'username'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(username in response_text)

    @freeze_time('2023-07-17')
    def test_get_correct_weekdate(self):
        '''при тестировании установить дату любого понедельника в декораторе'''
        username = 'username'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue('понедельник' in response_text)



