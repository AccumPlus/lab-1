from flask import Flask
from flask import request
from controller import Controller

totalNum = 2

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		num = request.args.get('num', '')
		return Controller.getHtml(int(num), totalNum)
