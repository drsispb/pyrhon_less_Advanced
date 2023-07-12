'''Задача 7. Учёт финансов
Что нужно сделать
Реализуйте приложение для учёта финансов, умеющее запоминать, сколько денег было потрачено за день,
а также показывать затраты за отдельный месяц и за целый год.

В программе должно быть три endpoints:

/add/<date>/<int:number> — сохранение информации о совершённой в рублях трате за какой-то день;
/calculate/<int:year> — получение суммарных трат за указанный год;
/calculate/<int:year>/<int:month> — получение суммарных трат за указанные год и месяц.
Дата для /add/ передаётся в формате YYYYMMDD, где YYYY — год, MM — месяц (от 1 до 12), DD — число (от 01 до 31).
Гарантируется, что переданная дата имеет такой формат и она корректна (никаких 31 февраля).'''

from flask import Flask
import time

app = Flask(__name__)


def check_date(date: int) -> bool:
    if len(str(date)) == 8:
        cnt = 0
        for_check_date = ''

        for i_elem in str(date):
            cnt += 1
            if cnt == 5 or cnt == 7:
                for_check_date += '/'
            for_check_date += i_elem
        try:
            valid_date = time.strptime(for_check_date, '%Y/%m/%d')
        except ValueError:
            print('Invalid date!')
        return True
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
