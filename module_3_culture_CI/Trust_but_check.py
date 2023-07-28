'''Задача 4. Доверяй, но проверяй
Что нужно сделать
Каждый разработчик ещё и тестировщик: он должен уметь покрыть тестами свой код. Но бывают ситуации,
когда он не успевает и просит помочь в этом деле своего товарища тестировщика. Вот и сейчас так получилось:
код есть, но тестами он не покрыт. Да и, кажется, писался он впопыхах пальцем левой ноги, надо бы его проверить.

Покройте данный класс юнит-тестами: все методы должны быть проверены.
Используя написанные тесты, найдите ошибки и исправьте их.
Найденные ошибки и их исправления оформите в виде Markdown-файла ERRORS.MD.
'''
import datetime

class Person:
    def __init__(self, name, year_of_birth, address=''):
        self.name = name
        self.yob = year_of_birth
        self.address = address

    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.yob

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = self.name

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address

    def is_homeless(self):
        if len(self.address) > 1:
            return False
        else:
            return True

