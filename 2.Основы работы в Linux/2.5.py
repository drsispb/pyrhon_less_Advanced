'''Задача 5. Максимальное число
Что нужно сделать
Реализуйте endpoint, начинающийся с /max_number, в который можно передать список чисел, разделённых слешем /.
Endpoint должен вернуть текст «Максимальное переданное число {number}», где number — выделенное курсивом наибольшее
из переданных чисел.

Примеры:

/max_number/10/2/9/1
Максимальное число: 10

/max_number/1/1/1/1/1/1/1/2
Максимальное число: 2'''



from flask import Flask

app = Flask(__name__)

@app.route("/max_number/<path:num_string>")
def hello_function_num(num_string: str) -> str:
    num_list = num_string.split('/')
    num_list_int = []
    for i_elem in num_list:
        try:
            num_list_int.append(int(i_elem))
        except:
            print('Не число ----', i_elem)
    max_num: int = max(num_list_int)
    return f'Max number <i>{max_num}</i>'


if __name__ == '__main__':
    app.run(debug=True)