'''Что нужно сделать
Напишите GET-endpoint /ps, который принимает на вход аргументы командной строки,
а возвращает результат работы команды ps с этими аргументами.

Входные значения endpoint должен принимать в виде списка через аргумент arg.

Например, для исполнения команды ps aux запрос будет следующим:
/ps?arg=a&arg=u&arg=x'''
import shlex

from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Email, NumberRange, Length
from wtforms import validators, Form, FormField
import os
from typing import List


app = Flask(__name__)


@app.route("/ps", methods=["GET"])
def ps():
    enter_list: List[str] = request.args.getlist('arg')
    clean_enter_list = [shlex.quote(elem) for elem in enter_list]
    exit_elem = ''.join(clean_enter_list)
    return exit_elem



if __name__ == '__main__':
    '''Для работы с postman'''
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True, port=5544)