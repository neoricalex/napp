from subprocess import Popen
import sys, pathlib

def iniciarFlask():
    while True:
        processo = Popen("python ./flask/app.py", shell=True)
        processo.wait()

def instalarMigrations():
    processo = Popen("python ./flask/bd.py db init", shell=True)
    processo.wait()

def instalarBD():
    migracoes = pathlib.Path('migrations')
    if migracoes.is_dir():
        processo = Popen("python ./flask/bd.py db migrate", shell=True)
        processo.wait()
    else:
        instalarMigrations()
        processo = Popen("python ./flask/bd.py db migrate", shell=True)
        processo.wait()

def atualizarBD():
    processo = Popen("python ./flask/bd.py db upgrade", shell=True)
    processo.wait()


if len(sys.argv) > 1:
    argumento = sys.argv[1] + '.py'
    processo = Popen("python " + argumento, shell=True)
    processo.wait()
else:
    base_de_dados = pathlib.Path('baseDeDados.db')
    if base_de_dados.is_file():
        iniciarFlask()
    else:
        instalarBD()
        atualizarBD()
        iniciarFlask()
