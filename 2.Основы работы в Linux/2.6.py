'''
Задача 6. Превью файла
Что нужно сделать
Реализуйте endpoint, который показывает превью файла, принимая на вход два параметра: SIZE (int) и RELATIVE_PATH — и
возвращая первые SIZE символов файла по указанному в RELATIVE_PATH пути.

Endpoint должен вернуть страницу с двумя строками.

В первой строке будет содержаться информация о файле: его абсолютный путь и размер файла в символах, а во
второй строке — первые SIZE символов из файла:

<abs_path> <result_size><br>
<result_text>

где abs_path — написанный жирным абсолютный путь до файла;
result_text — первые SIZE символов файла;
result_size — длина result_text в символах.

Перенос строки осуществляется с помощью HTML-тега <br>.

Пример:

docs/simple.txt:
hello world!

/preview/8/docs/simple.txt
/home/user/module_2/docs/simple.txt 8
hello wo

/preview/100/docs/simple.txt
/home/user/module_2/docs/simple.txt 12
hello world!
'''

from flask import Flask
import os
app = Flask(__name__)


@app.route("/preview/<int:SIZE>/<path:RELATIVE_PATH>")
def preview(SIZE: int, RELATIVE_PATH: str) -> str:
    path = os.path.abspath(os.path.join('../..', RELATIVE_PATH))
    with open(path, 'r') as file:
        preview = file.read(SIZE)
    cnt = 0
    for i_let in preview:
        cnt += 1
    return f'<b>{path}</b> {cnt} <br> {preview}'



if __name__ == '__main__':
    app.run(debug=True)