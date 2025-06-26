# CREAR LISTA DE USUARIOS

lista_usuarios = []
lista_genero = []
contraseñas = []

# CREAR DEF PARA DESARROLLAR EL CODIGO Y LLAMAR AL MOMENTO DEL MATCH - CASE

def ingresar_usuario():
    # USAMOS CICLO WHILE PARA REPETIR HASTA QUE LOS DATOS SEAN INGRESADOS CORRECTAMENTE
    
    while True:
        try:
            nombre = input("Ingrese su nombre de usuario: ").strip()
        except TypeError as e:
            print("Error de tipo.")
        if nombre in lista_usuarios:
            print("Usuario Repetido. Favor de elegir otro.")
        else:
            break
        lista_usuarios.append(nombre)
    
    while True:
        try:
            genero = input("\nIngrese su 'Género' indicando 'F' o 'M' para Femenino o Masculino: ").lower()
        except TypeError:
            print("Error de tipo.")
        if genero == "f" or genero == "m":
            lista_genero.append(genero)
            break
        else:
            print("Debe ingresar solo 'F' y/o 'M', Favor de re intentar.")
            
    while True:
        try:
            contraseña = input("\nIngrese su contraseña con un largo mínimo de 8 caracteres sin espacios:")
        except TypeError:
            print("Error de tipo.")
        if len(contraseña) < 8:
            print("La contraseña debe poseer un minimo de '8 Caracteres', Intentelo de nuevo.")
        elif " " == contraseña:
            print("La contraseña no debe contener espacios, Intentelo otra vez.")
        else:
            contraseñas.append(contraseña)
            print("Contraseña Valida.")
            print("\nEl Usuario ha sido ingresado correctamente.")
            break
 
def buscar_usuario():
    while True:
        nombre = input("Ingrese nombre de Usuario a buscar: ")
        encontrado = False # USAMOS UNA FLAG
        
        for i in range (len(lista_usuarios)):
            if lista_usuarios[i] == nombre:
                print("Usuario encontrado.")
                print(f"- Genero: {lista_genero[1]}\n - Contraseña: {contraseñas[1]}")
                encontrado = True
                break
        if not encontrado:
            print("Usuario no encontrado.")

def eliminar_usuario():
    nombre = input("Ingrese nombre de Usuario a Eliminar:")
    

# CREAR EL MENÚ PRINCIPAL 

while True:
    
    print("======================================")
    print("            MENÚ PRINCIPAL            ")
    print("\n1.- Ingresar Usuario.\n2.- Buscar Usuario.\n3.- Eliminar Usuario.\n4.- Salir.")
    print("======================================")
    
    try:
        opcion = int(input("Seleccione una opción del Menú Principal: "))
    except ValueError:
        print("Opción Incorrecta. Seleccione un número 'Entero Positivo' en el rango de 1 a 4.")
        continue
    except ZeroDivisionError:
        print("No divida por cero.")
        continue
    
    # UTILIZAR MATCH - CASE PARA DIVIDIR EL MENÚ EN SECCIONES ELEJIBLES ENTRE 1, 2, 3, 4 y _.
    
    match opcion:
        
        case 1:
            print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print("      INGRESO DE USUARIO      ")
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            ingresar_usuario()
            print("")
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        case 2:
            buscar_usuario()
            # SE PUEDEN UTILIZAR LOS INPUTS TANTO AFUERA DEL DEF COMO DENTRO DEL DEF. EN ESTE CASO LO USAMOS DENTRO PARA SIMPLICAR LA CODIFICACIÓN
        case 3: 
            eliminar_usuario()
            # SE PUEDEN UTILIZAR LOS INPUTS TANTO AFUERA DEL DEF COMO DENTRO DEL DEF. EN ESTE CASO LO USAMOS DENTRO PARA SIMPLICAR LA CODIFICACIÓN
        case 4:
            print("Finalizando Programa. Hasta pronto :). ")
            break
        case _:
            print("Caracter Invalido. Vuelva a Intentarlo usando Números entre 1 y 4.")