# ejercicio 1 Gestor de Tareas (To-Do List)

class Task:
    def __init__(self, name, due_date, priority):
        self.name = name
        self.due_date = due_date
        self.priority = priority

# Creamos una lista para almacenar las tareas
task_list = []

# Función para agregar una tarea a la lista
def add_task(name, due_date, priority):
    new_task = Task(name, due_date, priority)
    task_list.append(new_task)

# Función para editar una tarea en la lista
def edit_task(index, name, due_date, priority):
    task_list[index].name = name
    task_list[index].due_date = due_date
    task_list[index].priority = priority

# Función para eliminar una tarea de la lista
def delete_task(index):
    del task_list[index]
