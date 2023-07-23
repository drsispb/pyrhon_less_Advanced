'''Задача 3. Учёт финансов
Что нужно сделать
К деньгам стоит подходить ответственно, поэтому давайте протестируем наше приложение «Учёт финансов» из предыдущего модуля:

Заполните storage изначальными данными, с которыми вы будете работать в каждом тесте.
Проверьте, что endpoint /add/ работает.
Проверьте, что оба endpoints /calculate/ работают.
Проверьте, что endpoint /add/ может принять дату только в формате YYYYMMDD, а при подаче невалидного значения
что-то идёт не так. Нужно добиться такого условия, при котором endpoint свалится с ошибкой.
Проверьте, как будут работать endpoints /calculate/, если в storage ничего нет.
Советы и рекомендации
Проверить, порождает ли какое-то действие исключение, можно с помощью менеджера контекста assertRaises:
with self.assertRaises(TypeError):
# здесь то, что должно выбросить исключение TypeError
Создавать общие для всех тестов данные лучше в методе setUpClass.
@classmethod
def setUpClass(cls):
    storage.update(...)'''

from flask import Flask
import time

app = Flask(__name__)


def check_date(date: int) -> bool:
    if len(str(date)) == 8:
        try:
            time.strptime(str(date), '%Y%m%d')
            return True
        except ValueError:
            print('Invalid date!')
            return False
    else:
        return False


total: dict = {}


@app.route("/add/<date>/<int:number>")
def add(date: int, number: int) -> str:
    if check_date(date) and isinstance(number, int):
        global total
        if date not in total:
            total[date] = number
        else:
            total[date] += number
    else:
        return 'Ошибка даты или суммы'
    return f'Вы добавили расход в размере {number}, на дату {date}'


@app.route("/calculate/<int:year>")
def calculate(year: int) -> str:
    global total
    summ = 0
    for i_key, i_value in total.items():
        if str(i_key[:4]) == str(year):
            summ += i_value

    return f"Общая сумма трат за {year} год, составляет {summ}"


@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(year: int, month: int) -> str:
    global total
    summ = 0
    for i_key, i_value in total.items():
        if str(i_key[:6]) == str(year) + str(month):
            summ += i_value

    return f"Общая сумма трат за {month} месяц {year} года, составляет {summ}"


if __name__ == "__main__":
    app.run(port=5555, debug=True)
