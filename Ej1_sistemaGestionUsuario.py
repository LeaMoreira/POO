"""
elegi que la autenticacion no sea con nombre sino con email. porque los email asi como los dni son unicos,
lo cual permite que si hay usuarios que poseen el mismo nombre, como por ejemplo,
tengo un compañero que se llama igual que yo, lo cual la unica forma de diferenciarnos y poder registrarnos es mediante el email.
"""
import json
import hashlib

road_users = "usuarios.json"

def read_json():
    """
    Lee el contenido del archivo JSON su formato diccionario
    si el archivo no existe o esta vacio, devuelve un diccionario vacio
    
    Variables importantes:
    - road_users: La ruta del archivo JSON
    - file: El archivo JSON abierto en modo lectura
    
    Manejo de excepciones:
    - FileNotFoundError: Si el archivo no existe
    - json.JSONDecodeError: Si el archivo esta vacio o contiene datos no validos
    """
    try:
        with open(road_users, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def write_json(usuarios):
    """
    Escribe en el archivo JSON con formato indentado
    Unica diferencia con las variables de read_json es el ident=4 para espaciar la informacion y lea mas sencillo
    """
    with open(road_users, "w") as file:
        json.dump(usuarios, file, indent=4)

def hash_password(password):
    """
    Encripta la contraseña utilizando el algoritmo SHA-256 y devuelve el hash resultante
    
    Variables importantes:
    - password: La contraseña que ingresa el usuario
    - hash: El hash de la contraseña encriptada
    """
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(name, email, password):
    """
    Registra un nuevo usuario guardando su nombre, email y contraseña encriptada en el archivo JSON
    Si el email ya esta registrado, devuelve un mensaje de aviso
    
    Variables importantes:
    - name: El nombre del usuario
    - email: El correo electronico del usuario (clave unica)
    - password: La contraseña ingresada por el usuario
    - encrypt_password: La contraseña encriptada utilizando SHA-256
    - user_data: Un diccionario con el nombre y la contraseña encriptada del usuario, forma que tendra una vez lo escribimos en el json
    - usuarios: El diccionario de todos los usuarios leidos del archivo JSON
    
    Manejo de excepciones:
    - Verifica si el email ya existe en el diccionario "usuarios"
    """
    encrypt_password = hash_password(password)

    user_data = {
        "name": name,
        "password": encrypt_password
    }

    usuarios = read_json()

    if email in usuarios:
        return f"El correo {email} ya esta registrado."
    
    usuarios[email] = user_data
    
    write_json(usuarios)
    return f"Usuario {name} registrado con exito."

def authenticate_user(email, password):
    """
    Verifica si un email y una contraseña coinciden con algun usuario registrado en el archivo JSON
    Devuelve un mensaje de aviso si la autenticacion fue exitosa o no
    
    Variables importantes:
    - email: El correo electronico del usuario
    - password: La contraseña ingresada por el usuario
    - encrypt_password: La contraseña encriptada utilizando SHA-256
    - usuarios: El diccionario de todos los usuarios leidos del archivo JSON
    
    Manejo de excepciones:
    - Verifica si el email existe en el diccionario "usuarios"
    - Compara la contraseña encriptada con la guardada en el JSON
    """
    encrypt_password = hash_password(password)

    usuarios = read_json()
    
    if email in usuarios:
        if usuarios[email]["password"] == encrypt_password:
            return "Autenticacion exitosa."
        else:
            return "Contraseña incorrecta."
    else:
        return f"El correo {email} no está registrado."

while True:
    """
    Bucle que interactua con las funciones realizadas y permite al usuario registrar un nuevo usuario,
    autenticar un usuario existente o salir del programa
    
    Variables importantes:
    - option: La opcion elegida por el usuario en el menu
    - name: El nombre del usuario ingresado (para registro)
    - email: El correo electronico ingresado por el usuario (para registro y autenticacion)
    - password: La contraseña ingresada por el usuario (para registro y autenticacion)
    - data: El mensaje de resultado de las funciones "register_user" y "authenticate_user"
    """
    print("\n1. Registrar Usuario")
    print("2. Autenticar Usuario")
    print("3. Salir")

    option = input("Elige una Opcion: ")

    if option == "1":
        name = input("Nombre Usuario: ")
        email = input("Email: ")
        password = input("Contraseña: ")
        data = register_user(name, email, password)
        print(data)
    elif option == "2":
        email = input("Email: ")
        password = input("Contraseña: ")
        data = authenticate_user(email, password)
        print(data)
    elif option == "3":
        break
    else:
        print(f"Opcion: {option} seleccionada no es valida.")