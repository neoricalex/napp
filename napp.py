from subprocess import Popen
import sys, pathlib

if len(sys.argv) > 1:
    primeiro_argumento = sys.argv[1] + '.py'
    processo = Popen("python " + primeiro_argumento, shell=True)
else:
    base_de_dados = pathlib.Path('database.db')
    if base_de_dados.is_file():
        while True:
            processo = Popen("python myapp.py", shell=True)
            processo.wait()
    else:
        print('A base de dados não existe!')