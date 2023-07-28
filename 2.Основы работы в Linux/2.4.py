'''Задача 4. Хорошего дня!
Что нужно сделать
Реализуйте endpoint /hello-world/<имя>, который возвращает строку «Привет, <имя>.
Хорошей пятницы!». Вместо хорошей пятницы endpoint должен уметь желать хорошего дня недели в целом, на русском языке.

Пример запроса, сделанного в субботу:

/hello-world/Саша  →  Привет, Саша. Хорошей субботы!'''


from flask import Flask
from datetime import datetime

app = Flask(__name__)



weekdays_tuple = ('Хорошего понедельника', 'Хорошего вторника', 'Хорошей среда', 'Хорошего четверга',
                  'Хорошей пятницы', 'Хорошей субботы', 'Хорошего воскресенья')


# weekdays_list = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Cуббота', 'Воскресенье']

# weekdays_dict = {0: 'Понедельник', 1: 'Вторник', 2: 'Среда', 3: 'Четверг', 4: 'Пятница', 5: 'Cуббота', 6: 'Воскресенье'}

# print(sys.getsizeof(weekdays_tuple))
# print(sys.getsizeof(weekdays_list))
# print(sys.getsizeof(weekdays_dict))
@app.route("/hello/<username>")
def hello(username):
    weekday = datetime.today().weekday()
    day = weekdays_tuple[weekday]
    return f'Привет, {username}. {day}!'



if __name__ == "__main__":
    app.run(debug=True, port=5555)