'''Задача 1. Валидаторы. Добавление
Что нужно сделать
В endpoint /registration добавьте все валидаторы, о которых говорилось в последнем видео:

email (текст, обязательно для заполнения, валидация формата);
phone (число, обязательно для заполнения, длина — десять символов, только положительные числа);
name (текст, обязательно для заполнения);
address (текст, обязательно для заполнения);
index (только числа, обязательно для заполнения);
comment (текст, необязательно для заполнения).
'''

from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Email, NumberRange, Length, DataRequired, Regexp
from wtforms import validators, Form, FormField
import os

app = Flask(__name__)


class RegistrationForm(FlaskForm, Form):
    email = StringField(validators=[InputRequired(), Email()])
    phone = StringField(validators=[InputRequired(), Length(min=10, max=10), Regexp(regex='^[+-]?[0-9]+$')])
    name = StringField(validators=[InputRequired()])
    address = StringField(validators=[InputRequired()])
    index = StringField(validators=[InputRequired(), Length(min=6, max=6), Regexp(regex='^[+-]?[0-9]+$')])
    comment = StringField()


@app.route("/registration", methods=["POST"])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        return f'Successfully registred {form.name.data} {form.email.data} with phone +7{form.phone.data}'

    return f"Invalid input {form.errors}", 400



if __name__ == '__main__':
    '''Для работы с postman'''
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True, port=5544)

