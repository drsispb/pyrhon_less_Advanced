'''Задача 2. Валидаторы. Создание
Что нужно сделать
Довольно неудобно использовать встроенный валидатор NumberRange для ограничения числа по его длине.
Создадим свой для поля phone.

По своей сути валидатор — это функция, которая на вход принимает форму и поле,
а в случае ошибки валидации выкидывает ValidationError.

def number_length(form: FlaskForm, field: Field):
    if ...:
        raise ValidationError
number = IntegerField(validators=[InputRequired(), number_length])

Также можно реализовать его с помощью класса:
class NumberLength:
    def __call__(self, form: FlaskForm, field: Field):
        if ...:
            raise ValidationError

number = IntegerField(validators=[InputRequired(), NumberLength()])
Создайте валидатор обоими способами. Валидатор должен принимать на вход параметры min и max — минимальная и
максимальная длина, а также опциональный параметр message (см. рекомендации к предыдущему заданию).'''
from urllib.parse import unquote_plus

from wtforms.validators import InputRequired, Email, NumberRange, ValidationError
from dataclasses import Field
from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, Form
from wtforms.validators import InputRequired, Email, NumberRange
from typing import Optional
import re

app = Flask(__name__)



"""function"""


# @app.route("/registration", methods=["POST"])
# def length():
#     field = request.get_data(as_text=True)
#     number = re.sub('[^0-9]', '', field)
#     try:
#         if len(number) != 10:
#             raise ValidationError
#     except:
#         return f'invalid {number}'



"""class"""
# class NumberLength:
#     def __call__(self, field):
#         if len(field) != 10:
#             raise ValidationError
#         else:
#             return 'OK'
# @app.route("/registration", methods=["POST"])
# def length():
#     length_check = NumberLength()
#     number = request.form.get('number')
#     return length_check(number)
"""function"""
#
# @app.route("/registration", methods=["POST"])
# def length(min=1111111111, max=9999999999):
#     message = 'Must be between %d and %d characters long.' % (min, max)
#
#     def _length(form, field):
#         l = field.data and len(field.data) or 0
#         if l < min or l > max:
#             raise ValidationError(message)
#
#     return _length
#
# class MyForm(Form):
#     name = StringField('Name', [InputRequired(), length(max=50)])


"""class"""
# class Length(object):
#     def __init__(self, min=1111111111, max=9999999999, message=None):
#         self.min = min
#         self.max = max
#         if not message:
#             message = 'Field must be between %i and %i characters long.' % (min, max)
#         self.message = message
#
#     def __call__(self, form, field):
#         l = field.data and len(field.data) or 0
#         if l < self.min or l > self.max:
#             raise ValidationError(self.message)
#
# length = Length

if __name__ == '__main__':
    '''Для работы с postman'''
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True, port=5535)

