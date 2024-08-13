import json
import math

load_Movie = "movie.json"

def load_Data(file_Name):
    """Lee el archivo Json donde se encuentran los usuarios, las peliculas y las calificaciones de las mismas

    Args:
        file_Name (str): Argumento que utilizamos en caso de que tengamos más de un json para leer
    """
    try:
        with open(file_Name, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return {}
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON.")
        return {}
    
def calculate_Similarity(data, user1=None, user2=None):
    """Calculamos la similitud entre un usuario al que queremos recomendar la película,
    en comparación con los otros usuarios que ya la hayan visto para encontrar el perfil que tenga relación

    Args:
        data (dict): Variable del archivo Json que leeremos para extraer las calificaciones de las películas de cada usuario
        user1 (str, optional): Identifica el primer usuario a comparar. Defaults to None.
        user2 (str, optional): Identifica el segundo usuario a comparar. Defaults to None.

    Returns:
        float: Retornará el valor de la comparación entre la similitud entre el usuario a recomendar y los otros.
    """
    if user1 and user2:
        rate_User1 = data["usuarios"].get(user1, {})
        rate_User2 = data["usuarios"].get(user2, {})

        rate_Movies = set(rate_User1.keys()) & set(rate_User2.keys())
        
        #print(f"Películas comunes entre {user1} y {user2}: {rate_Movies}")

        if not rate_Movies:
            return 0
        
        #print("calificaiones de", user1, ":", rate_User1)
        #print("calificaiones de", user2, ":", rate_User2)
        #print(rate_Movies)

        rate_List1 = []
        rate_List2 = []

        for movie in rate_Movies:
            rate_List1.append(rate_User1[movie])
            rate_List2.append(rate_User2[movie])
        # otra forma de hacer lista y que se añadan de otras listas   
        #rate_List1 = [rate_User1[movie] for movie in rate_Movies]
        #rate_List2 = [rate_User2[movie] for movie in rate_Movies]

        dot_Product = 0
        for a, b in zip(rate_List1, rate_List2):
            dot_Product += a * b
        #dot_Product = sum(a*b for a, b in zip(rate_List1, rate_List2))

        long1 = math.sqrt(sum(a * a for a in rate_List1))
        long2 = math.sqrt(sum(b * b for b in rate_List2))

        if long1 == 0 or long2 == 0:
            return 0 # hacemos que no se pueda dividir por 0 es decir la evitamos
        
        similarity = dot_Product / (long1 * long2)
        #print(f"Similitud entre {user1} y {user2}: {similarity}")

        return similarity
    else:
        users = list(data["usuarios"].keys())
        similarities = {}

        for i in range(len(users)):
            for j in range(i + 1, len(users)):
                user1 = users[i]
                user2 = users[j]
                similarity_User = calculate_Similarity(data, user1, user2)
                similarities[(user1, user2)] = similarity_User
                similarities[(user2, user1)] = similarity_User
        
        return similarities

def recommend_Movies(data, target_User):
    """Genera la recomendación de películas de acuerdo al usuario específico basándonos en la similitud que hay entre usuarios

    Args:
        data (dict): Diccionario de json donde están los datos guardados de los usuarios y sus calificaciones de películas
        target_User (str): Sirve para identificar al usuario para el que estamos generando la recomendación

    Returns:
        list: Lista con las películas recomendadas y sus puntuaciones, ordenadas por puntuación descendente
    """
    user_Rating = data["usuarios"].get(target_User, {})
    #print(f"Calificaciones del usuario {target_User}: {user_Rating}")

    all_Users = [user for user in data["usuarios"] if user != target_User]
    
    similarities = {}
    for user in all_Users:
        similarity = calculate_Similarity(data, target_User, user)
        similarities[user] = similarity

    # key=lambda es una funcion de sorted donde realizamos una funcion sin nombre con arguento x
    # donde x[1] nos devuelve el elemento siguiente, en este caso el nombre del usuario o pelicula y su nota, nos devuelve la nota
    sorted_Users = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
    #print(f"Usuarios ordenados por similitud: {sorted_Users}")

    movie_Scores = {}
    total_Similarity = {}

    for user, similarity in sorted_Users:
        if similarity <= 0:
            continue

        user_Data = data["usuarios"][user]
        for movie, rating in user_Data.items():
            if movie not in user_Rating or user_Rating[movie] == 0:
                if movie not in movie_Scores:
                    movie_Scores[movie] = 0
                    total_Similarity[movie] = 0

                movie_Scores[movie] += rating * similarity
                total_Similarity[movie] += similarity

    recommendations = {movie: movie_Scores[movie] // total_Similarity[movie] for movie in movie_Scores}
    sorted_Recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    #print(f"Recomendaciones calculadas: {sorted_Recommendations}")

    return sorted_Recommendations

data = load_Data(load_Movie)
recommendations_Movie = recommend_Movies(data, "gonzalo")
print("Recomendaciones para el usuario Gonzalo:", recommendations_Movie)
#calculate_Similarity(data, user1= "leandro", user2= "gonzalo")