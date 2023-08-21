'''Задача 3. Валидаторы. Тестирование
Что нужно сделать
Для каждого поля и валидатора в endpoint /registration напишите юнит-тест, который проверит корректность
работы валидатора. Таким образом, нужно проверить, что существуют наборы данных, которые проходят валидацию,
и такие, которые валидацию не проходят.

Советы и рекомендации
Тестировать форму можно с помощью тестового клиента Flask, посылая POST-запросы к endpoint.'''


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
