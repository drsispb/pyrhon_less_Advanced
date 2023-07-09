import datetime
from flask import Flask

app = Flask(__name__)
counter = 0


@app.route('/test')
def test_function():
    return 'Это тестовая страничка, ответ сгенерирован в %s' % \
           datetime.datetime.now().utcnow()


@app.route('/hello_world')
def hello_function():
    return 'Hello world!'


@app.route('/counter')
def counter_function():
    global counter
    counter += 1
    return f'{counter} раз вызывалась эта страница'
