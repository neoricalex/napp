from flask import Flask
from flask_sqlalchemy import SQLAlchemy

ip = '0.0.0.0'
porta = '5000'

app = Flask(__name__)
app.config.from_pyfile('../config.py')
db = SQLAlchemy(app)

#from views import *

if __name__ == '__main__':
    app.run(host=ip, port=porta)