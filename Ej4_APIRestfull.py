import json

road_Task = "task.json"

def load_Tasks(file_Name):
    """
    Lee y carga datos de un archivo JSON
    
    Parametros:
    file_Name (str): Argumento donde se podra elegir que Json leer

    Return:
    list: Una lista de numeros leida desde el archivo JSON, o una lista vacia si ocurre un error
    """

    try:
        with open(file_Name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}
    
def save_Tasks(file_Name, task):


    with open(file_Name, "w") as file:
        json.dump(task, file, indent= 4)


def create_Tasks(task_Name, status):

    tasks= load_Tasks(road_Task)

    tasks[task_Name]= status

    save_Tasks(road_Task, tasks)
    print(f"Tarea '{task_Name}' creada con éxito.")
    input("Presione Enter para continuar...")

def read_Tasks():
    
    tasks = load_Tasks(road_Task)
    if tasks:
        print("Tareas: ")
        for task, status in tasks.items():
            print(f"{task}: {status}")
    else:
        print("No se encontraron tareas")
    
    input("Presione Enter para continuar...")

def update_Tasks(tasks_Name, new_Status):

    tasks = load_Tasks(road_Task)

    if tasks_Name in tasks:
        tasks[tasks_Name] = new_Status
        save_Tasks(road_Task, tasks)
        print(f"Tarea '{task_Name}' actualizada con éxito.")
    else:
        print(f"Tarea {tasks_Name}, no encontrada")
    input("Presione Enter para continuar...")

def delete_Tasks(task_Name):

    tasks= load_Tasks(road_Task)
    
    if task_Name in tasks:
        del tasks[task_Name]
        save_Tasks(road_Task, tasks)
        print(f"Tarea '{task_Name}' eliminada con éxito.")
    else:
        print(f"Tarea {task_Name}, no encontrada")
    input("Presione Enter para continuar...")

while True:
    print("")
    print("Sistema Interactivo de Tarea")
    print("")
    print("Para utilizar los comandos debera elegir alguna de las opciones")
    print("\n1: Para leer las tareas del archivo")
    print("2: Para crear una nueva tarea")
    print("3: Para actualizar una tarea")
    print("4: Para borrar una tarea")
    print("5: Para salir")

    opcion= input("Seleccione una Opcion: ")

    if opcion== "1":
        print(read_Tasks())
    elif opcion== "2":
        task_Name = input("Nombre una nueva tarea: ")
        status = input("Cual es el estado de esta tarea? ")
        create_Tasks(task_Name, status)
    elif opcion== "3":
        task_Name = input("Ingresa el nombre de la tarea: ")
        new_Status = input("Ingresa su nuevo estado: ")
        update_Tasks(task_Name, new_Status)
    elif opcion== "4":
        task_Name= input("Cual es la tarea a borrar: ")
        delete_Tasks(task_Name)
    elif opcion== "5":
        break
    else:
        print(f"opcion {opcion} invalida")
        input("Presione Enter para continuar...")