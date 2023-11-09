import json

#--------------- Variables Globales ------------------#
intentos = 0
cuentas = 0     #contador de cuentas creadas
usuarios = [[[], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], []]]     #matriz para guardar a los usuarios y passwords
#usuarios = [[[" ", " ", " ", " ", " ", " ", " ", " "], 
#             [" ", " ", " ", " ", " ", " ", " ", " "], 
#             [" ", " ", " ", " ", " ", " ", " ", " "], 
#             [" ", " ", " ", " ", " ", " ", " ", " "], 
#             [" ", " ", " ", " ", " ", " ", " ", " "], 
#             [" ", " ", " ", " ", " ", " ", " ", " "], 
#             [" ", " ", " ", " ", " ", " ", " ", " "], 
#             [" ", " ", " ", " ", " ", " ", " ", " "], 
#             [" ", " ", " ", " ", " ", " ", " ", " "]], 
#            [[" ", " ", " ", " ", " ", " ", " ", " "], 
#             [" ", " ", " ", " ", " ", " ", " ", " "], 
#             [" ", " ", " ", " ", " ", " ", " ", " "], 
#             [" ", " ", " ", " ", " ", " ", " ", " "], 
#             [" ", " ", " ", " ", " ", " ", " ", " "], 
#             [" ", " ", " ", " ", " ", " ", " ", " "], 
#             [" ", " ", " ", " ", " ", " ", " ", " "], 
#             [" ", " ", " ", " ", " ", " ", " ", " "], 
#             [" ", " ", " ", " ", " ", " ", " ", " "]]]     #matriz para guardar a los usuarios y passwords
preguntas = ["Cual es nombre de tu ciudad de nacimiento?", "Cual es tu numero favorito?"]
claves_seguridad = {}
dicc_usuarios = {}

#######################################################
#----------------- Funcionalidades -------------------#


def llenar_arrays():
    

    index_l1 = 0    #'index_l1' contador para cambiar de nivel donde existen usuarios y passwords
    index_l2 = 0    #'index_l2' contador para cambiar cada entrada de ya sea de usuarios o passwords
    for tipo in usuarios:   #'tipo'- usuarios o passwords 
        for entrada in tipo:    #entrada- cada entrada de 'tipo'
            usuarios[index_l1][index_l2] = dar_formato("")  #formatea cada entrada con ["z", "z", "z", "z", "z", "z", "z", "z"] 
            index_l2 += 1   #cambia a la siguiente entrada dentro de 'tipo'

        index_l2 = 0    #vuelve a la primera entrada de 'tipo'
        index_l1 += 1   #cambia a la siguiente parte de tipo



def dar_formato(cadena):
    arreglo = [" ", " ", " ", " ", " ", " ", " ", " "]  #formato de cadena para llenar
    
    index = 0   #indice para cada caracter de 'cadena'
    for letra in cadena:    #itera en cada caracter de la 'cadena' dada
        arreglo[index] = letra  #asigna el caracter actual a la posicion 'index' de 'arreglo'
        index += 1  #cambia al siguiente indice

    return arreglo      #retorna el cadena en formato separado caracter por caracter



def reconstruir(arreglo):
    palabra = ""    #'palabra' - variable que guarda la palabra reconstruida

    for letra in arreglo:   #itera cada entrada de 'arreglo'
        palabra += letra    #agrega el valor actual de 'arreglo' a palabra

    return palabra      #retorna la palabra reconstruida



def comparar_arrays(array_1, array_2):
    index = 0   #'index' - variable para guardar la posicion de cada caracter de 'array_1' y 'array_2' que se van a comparar 
    for letra in array_1 :      #itera en cada caracter de 'array_1' , guarda su valor en letra
        if letra != array_2[index]:     #compara letra con el elemento de 'array_2' de la posicion 'indice'
            return False    #si se pierde la coincidencia de los caracteres en ambos arreglos se retorna False
        
        index += 1      #cambia al siguiente indice de 'array_2'

    return True     #si no hubo ninguna disparidad en los arreglos, retorna True

    

def validar_longitud(cadena):
    longitud = 0
    for letra in cadena:
        longitud += 1
    if longitud < 1 or longitud > 8 :
        return False
    
    return True



def validar_existencia(array):
    for entrada in usuarios[0]:
        if comparar_arrays(array, entrada):
            return True
    
    return False



def eliminar_entrada(array):
    global cuentas
    encontrado = False
    index = 0

    for usuario in usuarios[0]:
        if encontrado:
            usuarios[0][index] = usuarios[0][index + 1]
            usuarios[1][index] = usuarios[1][index + 1]
        elif comparar_arrays(array, usuario):
            encontrado = True
            cuentas -= 1
            index -= 1
        
        index += 1
        if index > 7:
            return



def separar_numeros(cadena):
    cadena += ","
    arreglo_final = []
    numero = ""
    for letra in cadena:
        if letra != "," and letra != " ":
            numero += letra
        elif letra == "," and numero != "":
            arreglo_final.append(int(numero))
            numero = ""

    return arreglo_final



def escribir_json(diccionario, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        json.dump(diccionario, archivo)



def leer_json(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        datos_json = json.load(archivo)
    return datos_json



def json_a_matriz():
    global cuentas
    contador = 0

    for user,password in dicc_usuarios.items():
        usuarios[0][contador] = dar_formato(user)
        usuarios[1][contador] = dar_formato(password)

        contador += 1

    cuentas = contador



#######################################################
#---------------- Submenu Principal ------------------#



def login():
    usuario = input("\nUsuario: ")
    password = input("Contraseña: ")

    if usuario == '' or password == '' :
        print('\nNo puede dejar campos vacios\n')
        return

    index = 0
    for cuenta in usuarios[0]:
        if dar_formato(usuario) == cuenta and usuarios[1][index] == dar_formato(password):
            print("\nInicio de sesión exitoso. ¡Bienvenido,", usuario, "!")
            input("Presione Enter para continuar")
            logged()
            return

        index +=1

    print("\nCredenciales incorrectas.")


def crear_cuenta():
    global cuentas

    if cuentas == 8:
        print("\nError: El limite de cuentas se ha alcanzado")
        return
    

    usuario = input("\nNuevo usuario: ")

    if not validar_longitud(usuario):
        print("\nError: Su entrada debe tener entre 1 y 8 caracteres \n")
        return

    if validar_existencia(dar_formato(usuario)):
        print("\nEl usuario ya existe.")
        return
    
    password = input("Nueva contraseña: ")

    if not validar_longitud(password):
        print("\nError: Su entrada debe tener entre 1 y 8 caracteres \n")
        return
    else:
        usuarios[0][cuentas] = dar_formato(usuario)
        usuarios[1][cuentas] = dar_formato(password)

        dicc_usuarios[usuario] = password
        escribir_json(dicc_usuarios, 'usuarios.json')

        salir = False
        while not salir:
            print(preguntas[0])
            ciudad = input("--> ").strip()

            print(preguntas[1])
            numero = input("--> ").strip()

            print("Los datos son correctos?")
            print("Ciudad: ", ciudad)
            print("Numero: ", numero)
            print("\n\n1.-Si\n2.-No")
            op = input("-->  ")
            if op == "1" :
                claves_seguridad[cuentas] = {}
                claves_seguridad[cuentas]["ciudad"] = ciudad
                claves_seguridad[cuentas]["numero"] = numero

                escribir_json(claves_seguridad, "claves.json")
                salir = True
            else:
                print("Por favor, vuelva a escribir sus datos")

        cuentas += 1
        print("\nCuenta creada exitosamente.")

        imprimir_usuarios()



def imprimir_usuarios():

    if cuentas == 0:
        print("\nNo hay usuarios registrados todavia")
        return False
    

    index = 0   #

    print("\nUsuarios:\n")
    for array_usuario in usuarios[0]:   #itera en los elementos de usuarios, asigna el array actual de usuarios a 'array_usuarios'
        array_password = usuarios[1][index]     #asigna el password correspondiente al indice actual a 'array_password'
        if array_usuario != dar_formato('') :        #
            print(reconstruir(array_usuario) + " " + reconstruir(array_password))
        
        index += 1
    
    return True



def borrar_usuario():

    if not imprimir_usuarios():
        return
    
    objetivo = input("Escriba el nombre del usuario que desea eliminar:\n--> ")

    if not validar_existencia(dar_formato(objetivo)):
        print("Usuario no valido o inexistente\n")
        return
    
    print("Se va a eliminar el usuario " + objetivo + ", Desea continuar?")
    print("1. Si")
    print("2. No")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        eliminar_entrada(dar_formato(objetivo))
        print("Usuario borrado correctamente")
    else:
        print("Operacion cancelada")
        return



##############################################################
#------------------ Submenu Algoritmos ----------------------#


def burbuja():
    arreglo = separar_numeros(input("Digite una serie de numeros desordenados \nseparados por comas: \n-->"))

    iteraciones = 0
    consultas = 0
    cambios = 0

    for iteracion in range(len(arreglo)):
        iteraciones += 1
        for indice in range(len(arreglo) - 1):
            indice_siguiente = indice + 1

            consultas += 1
            if arreglo[indice] > arreglo[indice_siguiente]:
                cambios += 1
                temporal = arreglo[indice_siguiente]
                arreglo[indice_siguiente] = arreglo[indice]
                arreglo[indice] = temporal

    print(f'Arreglo ordenado: {arreglo}')
    print(f'Iteraciones: {iteraciones}')
    print(f'Consultas: {consultas}')
    print(f'Cambios: {cambios}')


def burbuja_mejorado():
    arreglo = separar_numeros(input("Digite una serie de numeros desordenados \nseparados por comas: \n-->"))

    iteraciones = 0
    consultas = 0
    cambios = 0
    salida = False

    while salida == False:

        salida = True
        iteraciones += 1
        for indice in range(len(arreglo) - iteraciones):

            indice_siguiente = indice + 1
            consultas += 1
            if arreglo[indice] > arreglo[indice_siguiente]:
                cambios += 1
                salida = False

                temporal = arreglo[indice_siguiente]
                arreglo[indice_siguiente] = arreglo[indice]
                arreglo[indice] = temporal

    print(f'Arreglo ordenado: {arreglo}')
    print(f'Iteraciones: {iteraciones}')
    print(f'Consultas: {consultas}')
    print(f'Cambios: {cambios}')



def insertion():
    
    arreglo = separar_numeros(input("Digite una serie de numeros desordenados \nseparados por comas: \n-->"))


    iteraciones = 0
    consultas = 0
    cambios = 0

    iteraciones += 1
    for posicion_actual in (range(1, len(arreglo))):

        puntero = posicion_actual
        temporal = arreglo[posicion_actual]
        i = 1
        mayor = True

        while mayor == True and posicion_actual - i >= 0:

            consultas += 1
            if arreglo[posicion_actual - i] > temporal:

                cambios += 1
                arreglo[puntero] = arreglo[puntero - 1]
                i += 1
                puntero -= 1

            else:
                mayor = False

        arreglo[puntero] = temporal

    print(f'Arreglo ordenado: {arreglo}')
    print(f'Iteraciones: {iteraciones}')
    print(f'Consultas: {consultas}')
    print(f'Cambios: {cambios}')



def quicksort_ejecucion():
    
    iteraciones = 0
    comparaciones = 0
    intercambios = 0
    valores = 0

    def quicksort_nucleo(arreglo):
        nonlocal iteraciones, comparaciones, intercambios, valores

        comparaciones += 1
        
        if len(arreglo) <= 1:
            return arreglo
        else:
            pivote = arreglo[-1]
            intercambios += 1
            menores = [x for x in arreglo[:-1] if x < pivote]
            mayores = [x for x in arreglo[:-1] if x >= pivote]
            valores += 2 * (len(arreglo) - 1)
            return quicksort_nucleo(menores) + [pivote] + quicksort_nucleo(mayores)
        

    arreglo = separar_numeros(input("Digite una serie de numeros desordenados \nseparados por comas: \n-->"))
    
    arreglo_ordenado = quicksort_nucleo(arreglo)
    iteraciones = valores / len(arreglo)

    print(f'Arreglo ordenado: {arreglo_ordenado}')
    print(f'Iteraciones: {iteraciones}')
    print(f'Consultas: {comparaciones}')
    print(f'Cambios: {intercambios}')



def algoritmos():
    while True:
        print("\nMenu:")
        print("1. Algoritmo Burbuja")
        print("2. Algoritmo Burbuja mejorado")
        print("3. Algoritmo Insertion")
        print("4. Algoritmo QuickSort")
        print("5. Regresar al menu de login")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print("Alogoritmo Burbuja:\n")
            burbuja()
        elif opcion == "2":
            print("Alogoritmo Burbuja Mejorado:\n")
            burbuja_mejorado()
        elif opcion == "3":
            print("Alogoritmo Insertion:\n")
            insertion()
        elif opcion == "4":
            print("Alogoritmo QuickSort:\n")
            quicksort_ejecucion()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")



##############################################################
#------------------- Submenu Logueado -----------------------#

def logged():
    while True:
        print("\nMenu:")
        print("1. Probar Algoritmos de Ordenamiento")
        print("2. Editar Usuario")
        print("3. Cerrar Sesion")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            algoritmos()
        elif opcion == "2":
            #funcion de editar usuario
            input() 
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")



#############################################################
#------------------------- Main ----------------------------#


def main():
    while True:
        print("\nMenu:")
        print("1. Iniciar sesión")
        print("2. Crear cuenta")
        print("3. Visualizar usuarios")
        print("4. Borrar usuario")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            login()
        elif opcion == "2":
            crear_cuenta()
        elif opcion == "3":
            imprimir_usuarios()
        elif opcion == "4":
            borrar_usuario()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")



if __name__ == "__main__":
    llenar_arrays()
    try:
        claves_seguridad = leer_json('claves.json')
        dicc_usuarios = leer_json('usuarios.json')
    except FileNotFoundError:
        print("Sin datos que cargar\n\n\n\n")
    
    json_a_matriz()
    main()
