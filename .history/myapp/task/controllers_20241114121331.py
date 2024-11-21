from flask import Blueprint, render_template, request, redirect, url_for

taskRoute = Blueprint('task', __name__, url_prefix='/task')  # Uso de __name__ en lugar de _name_
task_list = ['tasks 1', 'tasks 2', 'tasks 3']

# Ruta para mostrar todas las tareas
@taskRoute.route('/')
def index():
    return render_template('dashboard/task/index.html', tasks=task_list)

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
    task = request.form.get('task')
    if task is not None and task != "":  # verifica que no venga vacia 
        task_list.append(task)
        return redirect(url_for('task.index'))
    return render_template('dashboard/task/create.html')

# Ruta para actualizar una tarea específica
@taskRoute.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id: int):
    task = request.form.get('task')
    if task is not None and task != "" and 0 <= id < len(task_list):  # Verificación de índice válido
        task_list[id] = task
        return redirect(url_for('task.index'))
    return render_template('dashboard/task/update.html')
