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
from wtforms import StringField, IntegerField
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


if __name__ == '__main__':
    '''Для работы с postman'''
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True, port=5535)

