'''Задача 4. Время работы системы
Что нужно сделать
Напишите GET-endpoint /uptime, который в ответ на запрос будет выводить строку вида

f"Current uptime is {UPTIME}"

где UPTIME — uptime системы (показатель того, как долго текущая система не перезагружалась).
Сделать это можно с помощью команды uptime.'''

from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Email, NumberRange
import os
import subprocess

app = Flask(__name__)


@app.route("/uptime", methods=["GET"])
def uptime():
    cmd = "uptime", "-p"
    UPTIME = subprocess.check_output(cmd).decode("utf-8")
    return f"Current uptime is {UPTIME}"


if __name__ == '__main__':
    '''Для работы с postman'''
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True, port=5555)
