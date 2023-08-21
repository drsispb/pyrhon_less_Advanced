'''Что нужно сделать
Напишите GET-endpoint /ps, который принимает на вход аргументы командной строки,
а возвращает результат работы команды ps с этими аргументами.

Входные значения endpoint должен принимать в виде списка через аргумент arg.

Например, для исполнения команды ps aux запрос будет следующим:
/ps?arg=a&arg=u&arg=x'''
import shlex
import subprocess
from flask import Flask, request
from typing import List
import string
from sys import stdout


app = Flask(__name__)


@app.route("/ps", methods=["GET"])
def ps():
    enter_list: List[str] = request.args.getlist('arg')
    clean_enter_list = [shlex.quote(prefix) for prefix in enter_list]
    command_str = f"ps {' '.join(clean_enter_list)}"
    command = shlex.split(command_str)
    result = subprocess.run(command, capture_output=True)

    if result.returncode != 0:
        return 'error', 500
    output = result.stdout.decode()
    return string.Template(f"<pre>$output</pre>").substitute(output=output)




if __name__ == '__main__':
    '''Для работы с postman'''
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True, port=5544)