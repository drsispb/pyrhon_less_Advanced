import random
import datetime
from flask import Flask
import os
import re

app = Flask(__name__)
counter = 0

'''Задача 1. /hello_world
Что нужно сделать
Создайте страницу с текстом «Привет, мир!».'''

@app.route('/hello/world')
def hello_function():
    return 'Hello world!'

'''Задача 2. /cars
Что нужно сделать
Создайте страницу, возвращающую список машин через запятую: Chevrolet, Renault, Ford, Lada.'''

@app.route('/cars')
def cars():
    global cars
    cars = ['Chevrolet', 'Renault', 'Ford', 'Lada']
    str_car = ', '.join(cars)
    return str(str_car).translate({ord(i): None for i in '[]'})


'''Задача 3. /cats
Что нужно сделать
Создайте страницу с названием случайной породы кошек из следующего списка: корниш-рекс, русская голубая, 
шотландская вислоухая, мейн-кун, манчкин.'''

@app.route('/cats')
def cats():
    cats_list =['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']
    choise = random.choice(cats_list)
    return f'Данная страница посвещена следующей породе: {choise}'

'''Задача 4. /get_time/now
Что нужно сделать
Создайте страницу с текстом «Точное время: {current_time}», где current_time — точное текущее время.'''

@app.route('/get_time/now')
def get_time_now():
    current_time = datetime.datetime.now()
    return f'«Точное время: {current_time}»'

'''Задача 5. /get_time/future
Что нужно сделать
Создайте страницу с текстом «Точное время через час будет {current_time_after_hour}», 
где current_time_after_hour — точное время через один час.'''

@app.route('/get_time/future')
def get_time_future():
    current_time = datetime.datetime.now()
    current_time_after_hour = current_time + datetime.timedelta(hours=1)
    return f'«Точное время через час будет: {current_time_after_hour}»'

'''Задача 6. /get_random_word
Что нужно сделать
Создайте страницу со случайным словом из книги «Война и мир» Льва Толстого. 
Книга лежит в одной папке с практическим заданием и называется war_and_peace.txt.'''

@app.route('/get_random_word')
def get_random_word():
    with open('war_and_peace.txt', 'r') as book:
        book_read = book.read()
        return random.choice(book_read.translate({ord(i): None for i in '.!«,»'}).split())


'''Задача 7. /counter
Что нужно сделать
Создайте страницу с числом, показывающим, сколько раз открывалась данная страница.'''
@app.route('/counter')
def counter_function():
    global counter
    counter += 1
    return f'{counter} раз вызывалась эта страница'