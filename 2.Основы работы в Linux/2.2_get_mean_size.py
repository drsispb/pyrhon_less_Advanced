'''
Задача 2. Средний размер файла
Что нужно сделать
Удобно направлять результат выполнения команды напрямую в программу с помощью конвейера (pipe):

$ ls -l | python3 get_mean_size.py

Напишите функцию get_mean_size, которая на вход принимает результат выполнения команды ls -l,
а возвращает средний размер файла в каталоге.
'''

import sys


def get_mean_size(object):
    total = 0
    cnt = 0
    for line in object:
        cnt += 1
        total += int(line.split()[4])
        average: float = round(total/cnt, 2)
    print(f'Cредний размер файла в каталоге {average}')


lines = sys.stdin.readlines()[1:]

get_mean_size(lines)
