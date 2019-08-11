from lib.funcoes import *

if checkarDB() == True:
    if checkarMigrations() == True:
        executarMigrations()
        atualizarMigrations()
    else:
        instalarMigrations()
        executarMigrations()
        atualizarMigrations()
else:
    if checkarMigrations() == True:
        executarMigrations()
        atualizarMigrations()
    else:
        instalarMigrations()
        executarMigrations()
        atualizarMigrations()

iniciarFlask()