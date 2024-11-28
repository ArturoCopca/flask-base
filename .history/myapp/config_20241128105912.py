import psycopg2
import os

ALLOWED_EXTENSIONS_FILES = {'pdf', 'jpg', 'jpeg', 'gif', 'png'}
def allowed_extensions_file(filename): #test.png
    return '.' in filename and filename.lower().rsplit('.',1)[1] in ALLOWED_EXTENSIONS_FILES
class Config(object):
    
    #Configuracion de las Bases de Datos
    #SQLite3:
    '''BASE_DIR =  os.path.abspath(os.path.dirname(__file__))
    DB_URI = "sqlite:///" + os.path.join(BASE_DIR, "database.db")'''
    #MySQL:
    '''DB_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(username="", password="", hostname="", databasename="")'''
    #PostgreSQL:
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://{username}:{password}@{hostname}/{databasename}".format(username="curso", password="12345", hostname="localhost", databasename="proyecto2")
