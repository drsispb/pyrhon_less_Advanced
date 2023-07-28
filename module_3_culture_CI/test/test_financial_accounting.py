'''Задача 3. Учёт финансов'''
import unittest
import time
from module_3_culture_CI.financial_accounting import app


total: dict = {20230101: 5000,
               20230115: 3000,
               20230226: 10000,
               20230308: 1000
               }

class TestFinancial(unittest.TestCase):

    def setUp(self) -> None:
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/'

    def test_add(self):
        add = 'add/'
        date = '20230501'
        number = '4000'
        response = self.app.get(self.base_url + add + date + '/' + number)
        response_text = response.data.decode()
        global total
        if date not in total:
            total[date] = number
        else:
            total[date] += number
        self.assertEqual(total[date], number)
        self.assertNotEqual(total[date], 1000)
        self.assertIn(number, response_text)
        self.assertIn(date, response_text)

    def test_calculate(self):
        calculate = 'calculate/'
        date = '2023'
        summ_test = '19000'
        summ_test2 = '0'
        response = self.app.get(self.base_url + calculate + date)
        response_text = response.data.decode()
        global total

        self.assertNotIn(summ_test, response_text)
        self.assertIn(summ_test2, response_text)
        self.assertIn(date, response_text)



    def test_calculate_month(self):
        calculate = 'calculate/'
        year = '2023'
        month = '3'
        summ_test = '19000'
        summ_test2 = '0'
        response = self.app.get(self.base_url + calculate + year + '/' + month)
        response_text = response.data.decode()
        global total

        self.assertNotIn(summ_test, response_text)
        self.assertIn(summ_test2, response_text)
        self.assertIn(year, response_text)
        self.assertIn(month, response_text)

