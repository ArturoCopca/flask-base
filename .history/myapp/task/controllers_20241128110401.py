import os
from flask import Blueprint, render_template, request, redirect, url_for, current_app
from myapp.task import operationsCRUD
from myapp.task import forms
from myapp import config
from werkzeug.utils import secure_filename

taskRoute = Blueprint('task', __name__, url_prefix='/task')  # Uso de __name__ en lugar de _name_


# Ruta para mostrar todas las tareas
@taskRoute.route('/')
def index():
    #print(operationsCRUD.getById(2).name)
    #print(operationsCRUD.getAll()[1].name)
    #print(operationsCRUD.delete(1))
    print(operationsCRUD.pagination().items)
    return render_template('dashboard/task/index.html', tasks=operationsCRUD.getAll())

# Ruta para mostrar una tarea específica por ID
@taskRoute.route('/<int:id>')
def show(id: int):
    return 'Show ' + str(id)

# Ruta para eliminar una tarea específica
@taskRoute.route('/delete/<int:id>')
def delete(id: int):
    if id is not None and 0 <= id < len(task_list):  # Verificación de índice válido
        del task_list[id]
    return redirect(url_for('task.index'))

# Ruta para crear una nueva tarea
@taskRoute.route('/create', methods=('GET', 'POST'))
def create():
      form = forms.Task()
    #se aplican las validaciones
    if form.validate_on_submit():
       operationsCRUD.create(form.name.data)
       
    return render_template('dashboard/task/create.html', form=form)

# Ruta para actualizar una tarea específica
@taskRoute.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id: int):
    task = request.form.get('task')
    if task is not None and task != "" and 0 <= id < len(task_list):  # Verificación de índice válido
        task_list[id] = task
        return redirect(url_for('task.index'))
    return render_template('dashboard/task/update.html')
