import json

road_List = "list_Num.json"  
road_List_Ordered = "list_Num2.json"  

def read_Json(file_Name):
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
        return []
    except json.JSONDecodeError:
        return []
    
def write_Json(file_Name, final_List):
    """
    Escribe una lista ordenada en un archivo JSON
    
    Parametros:
    file_Name (str): Argumento con nombre del archivo JSON donde se guardaran los datos
    ordered_List (list): Lista de numeros ordenada que se guardara en el archivo JSON
    """
    with open(file_Name, "w") as file:
        json.dump(final_List, file)

def merge_sort(original_List):
    """
    Aplica el algoritmo de Merge Sort para ordenar una lista de numeros
    
    Parametros:
    original_List (list): Lista de numeros que se desea ordenar

    Return:
    list: Una nueva lista ordenada de menor a mayor
    """
    if len(original_List) < 2:
        return original_List
    else:
        center = len(original_List) // 2

        list_1 = merge_sort(original_List[:center])
        list_2 = merge_sort(original_List[center:])

        return merge(list_1, list_2)

def merge(list_1, list_2):
    """
    Fusiona las dos sublistas ordenadas en una sola lista ordenada
    
    Parametros:
    list_1 (list): Primera sublista ordenada
    list_2 (list): Segunda sublista ordenada

    Retorna:
    list: Lista ordenada que resulta de fusionar "list_1" y "list_2"
    """
    ordered_List = []  # Lista final que contendra los elementos de list_1 y list_2 en orden
    a, b = 0, 0

    while a < len(list_1) and b < len(list_2):
        if list_1[a] < list_2[b]:
            ordered_List.append(list_1[a])
            a += 1
        else:
            ordered_List.append(list_2[b])
            b += 1

    if a == len(list_1):
        for c in range(b, len(list_2)):
            ordered_List.append(list_2[c])
    else:
        for c in range(a, len(list_1)):
            ordered_List.append(list_1[c])
    
    return ordered_List

def main():
    """
    Funcion principal que ejecuta el proceso de lectura, ordenacion y escritura de la lista
    """
    original_List = read_Json(road_List)

    final_List = merge_sort(original_List)

    write_Json(road_List_Ordered, final_List)

main()