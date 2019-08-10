from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('napp', MigrateCommand)

from views import *

if __name__ == '__main__':
    manager.run()
    app.run(host='0.0.0.0')