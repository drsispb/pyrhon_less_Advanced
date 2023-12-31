'''Задача 1. Хорошего дня!
Что нужно сделать
Мы кое-что забыли проверить, когда писали тест test_can_get_correct_username_with_weekdate: добавьте проверку
корректности вернувшегося дня недели.

Советы и рекомендации
Что будет, если программа выдаёт неправильный день недели, а в username передать строку ‘Хорошей среды’?
Тестировать только сегодняшний день будет неправильным — вдруг у программы семь пятниц на неделе. Но как это
сделать, если получение дня недели происходит в самой тестируемой функции? В этом поможет библиотека freezegun.
Протестируйте по крайней мере 7 дней.'''

from flask import Flask
from datetime import datetime

app = Flask(__name__)



weekdays_tuple = ('Хорошего понедельника', 'Хорошего вторника', 'Хорошей среда', 'Хорошего четверга',
                  'Хорошей пятницы', 'Хорошей субботы', 'Хорошего воскресенья')

@app.route("/hello/<username>")
def hello_day(username):
    weekday = datetime.today().weekday()
    day = weekdays_tuple[weekday]
    return f'Привет, {username}. {day}!'



if __name__ == "__main__":
    app.run(debug=True, port=5555)