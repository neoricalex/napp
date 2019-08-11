from lib.funcoes import checkarDB
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

print('Checkar se a base de dados existe ...')
checkarDB()

ip = '0.0.0.0'
porta = '5000'

app = Flask(__name__)
app.config.from_pyfile('./lib/config.py')
db = SQLAlchemy(app)

#from views import *

if __name__ == '__main__':
    app.run(host=ip, port=porta)