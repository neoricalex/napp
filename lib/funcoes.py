from subprocess import Popen
import sys, pathlib

def checkarDB():
    base_de_dados = pathlib.Path('baseDeDados.db')
    if base_de_dados.is_file():
        baseDeDados = True
    else:
        baseDeDados = False

    return baseDeDados

def checkarMigrations():
    migracoes = pathlib.Path('migrations')

    if migracoes.is_dir():
        migrations = True
    else:
        migrations = False
    
    return migrations

def instalarMigrations():
    processo = Popen("python lib/flask/migrations.py db init", shell=True)
    processo.wait()

def executarMigrations():
    processo = Popen("python lib/flask/migrations.py db migrate", shell=True)
    processo.wait()

def atualizarMigrations():
    processo = Popen("python lib/flask/migrations.py db upgrade", shell=True)
    processo.wait()

def iniciarFlask():
    processo = Popen("python lib/flask/app.py", shell=True)
    processo.wait()


    
    