''' Модуль сервера '''


from flask import Flask
from flask import request
from controller import Controller

TOTAL_NUM = 20
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    ''' Функция при переходе по корневому пути '''
    if request.method == 'GET':
        num = request.args.get('num', '')
        if num == '':
            num = 1
        return Controller.get_html(int(num), TOTAL_NUM)
