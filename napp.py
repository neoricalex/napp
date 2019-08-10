from subprocess import Popen
import sys, pathlib

def iniciarFlask():
    while True:
        processo = Popen("python myapp.py", shell=True)
        processo.wait()

def instalarBD():
    processo = Popen("python ./flask/bd.py db init", shell=True)
    processo.wait()
    processo = Popen("python ./flask/bd.py db migrate", shell=True)
    processo.wait()
    processo = Popen("python ./flask/bd.py db upgrade", shell=True)
    processo.wait()
    iniciarFlask()


if len(sys.argv) > 1:
    argumento = sys.argv[1] + '.py'
    processo = Popen("python " + argumento, shell=True)
    processo.wait()
else:
    base_de_dados = pathlib.Path('database.db')
    if base_de_dados.is_file():
        iniciarFlask()
    else:
        instalarBD()
