''' Este archivo se utiliza para realizar la importacion de las configuraciones globales
    tales como la importacion de la app, las rutas generales del proyecto, definir si el
    servidor corre en modo debug, Registro de la BD, etc.'''
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from myapp.config import DevConfig
from flask_migrate import Migrate

app = Flask(__name__) #template_folder="/pages"
#app.debug = True
app.config.from_object(DevConfig)

#Para la configuracion de la BD
db = SQLAlchemy(app)
from myapp.task.controllers import taskRoute
app.register_blueprint(taskRoute)
#Para la creacion de las tablas en la base de datos
with app.app_context():
    db.create_all()

@app.route('/')
def hello_world() -> str:
    name = request.args.get('name', 'Valor por defecto')
    return render_template('index.html', task="Arturo", name=name)