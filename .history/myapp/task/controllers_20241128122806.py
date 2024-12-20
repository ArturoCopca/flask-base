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
    return render_template('dashboard/task/index.html', task=operationsCRUD.getAll())

# Ruta para mostrar una tarea específica por ID
@taskRoute.route('/<int:id>')
def show(id: int):
    return 'Show ' + str(id)

# Ruta para eliminar una tarea específica
@taskRoute.route('/delete/<int:id>')
def delete(id: int):
    if id is not None and id is not "":
        operationsCRUD.delete(id)
        return redirect(url_for('task.index'))

# Ruta para crear una nueva tarea
@taskRoute.route('/create', methods=('GET', 'POST'))
def create():
    form = forms.Task()
    #se aplican las validaciones
    if form.validate_on_submit():
       operationsCRUD.create(form.name.data)
       return redirect(url_for('task.index'))
       
    return render_template('dashboard/task/create.html', form=form)

# Ruta para actualizar una tarea específica
@taskRoute.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id: int):
    
    task = operationsCRUD.getById(id, True)
    form = forms.Task()
    
    if request.method == 'GET':
        form.name.data = task.name
    
    if form.validate_on_submit():
        operationsCRUD.update(id, form.name.data)
        
        print(form.file.data)
        print(form.file.data.filename)
        f = form.file.data
        if f and config.allowed_extensions_file(form.file.data.filename):
            
            filename = secure_filename(f.filename)
            f.save(os.path.join(current_app.instance_path, current_app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('task.index'))
    return render_template('dashboard/task/update.html', form=form, id=id)
