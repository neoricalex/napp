from lib.funcoes import *

if checkarDB() == True:
    print('Iniciando o Flask ...')
else:
    if checkarMigrations() == True:
        executarMigrations()
    else:
        instalarMigrations()