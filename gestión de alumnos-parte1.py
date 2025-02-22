#En esta primera fase, creamos una estructura de datos para almacenar la información de cada alumno


#FUNCIONES:
def crear_alumno(numero_clase_local,nombre_alumno_local,apellido_alumno_local,alumnos_local):

    #declarar una lista de notas, por ahora vacía
    list_notas=[]

    print("-------------------------------------------------------------------")
    print("Desde este menú podrás inroducir la información de un nuevo alumno.\n\nDeberás introducir:\n->Su número de clase\n->Su nombre\n->Su apellido\n")
    print("Si deseas continuar escribe 'C'\nSi deseas volver al menú principal ecribe la letra 'R'")
    print("-------------------------------------------------------------------")
    
    #Pedimos un input para saber si continuar en el menú de crear alumno o volver al menú principal
    while True:
        input1=input().strip().upper() #modificamos el input para que siempre esté en mayúsculas y sin espacios al principio o al final

        #Si la entrada es R llamamos a la función main, la cual se ejecutará y mostrará el menú principal
        if (input1=="R"):
            main()

        #Si la entrada es C, continuamos al siguiente paso
        if (input1=="C"):
            print("-------------------------------------------------------------------")
            print("Introduce el número de clase del alumno")
            while True:
                numero_clase_local=input() #Pedimos el número por consola

                #Probamos a cambiar el valor introducido a un entero, si devuelve 'ValueError' sabemos que el valor introducido no era entero y volvemos a pedir una entrada
                try:
                    numero_clase_local=int(numero_clase_local) 
                except ValueError:
                    print("Entrada inválida, introduce un número\n")
                    continue #El continue nos devuelve al principio del while True en caso de no poder convertir el valor a entero
                
                #comprobar que el valor de número de clase no existe ya en el diccionario
                if(numero_clase_local in dict_alumnos):
                    print("-------------------------------------------------------------------")
                    print("\nEste número de clase ya existe. Para crear un nuevo alumno, introduce un número de clase nuevo")
                    print("-------------------------------------------------------------------")
                    continue #Continue nos devuelve al principio del while True en caso de que el número ya se encuentre en el diccionario

                #pedimos el nombre y apellido del alumno y cambiamos el formato a minúscolas sin espacios
                print("\nIntroduce el nombre del alumno")
                nombre_alumno_local=input().lower().strip()
                print("\nintroduce el apellido del alumno")
                apellido_alumno_local=input().lower().strip()

                #creamos un diccionario único para el alumno que permita almacenar la infomación en formato clave-valor
                dict_nuevo_alumno = {
                    "número": numero_clase_local,
                    "nombre": nombre_alumno_local,
                    "apellido": apellido_alumno_local,
                    "notas": list_notas
                }
                
                #Guardamos el diccionario personal del alumno nuevo dentro del el diccionario global de alumnos 
                #en el cual se identifica mediante su número de clase como clave única                
                alumnos_local[numero_clase_local] = dict_nuevo_alumno
                
                print("-------------------------------------------------------------------")
                print("\nPERFIL DE ALUMNO CREADO\n")

                #devolvemos el diccionario global actualizado con el nuevo alumno creado a la función main()
                return alumnos_local

        else:
            print("Entrada inválida, introduce la letra 'C' para continuar o la letra 'R' para volver al menú principal\n")


def leer_alumnos(dict_alumnos_local):
    print("-------------------------------------------------------------------")
    print("Desde este menú podrás: \n\n1. leer la información un alumno existente\n   ->Deberás introducir:Su número de clase para acceder a su información personal\n2. Leer la lista completa de alumnos junto a la infomación de cada uno")
    print("\nSi deseas continuar selecciona la opción 1 o 2\nSi deseas volver al menú principal ecribe la letra 'R'")
    print("-------------------------------------------------------------------")
    
    while True:
        input1=input().strip().upper() #modificamos el input para que siempre esté en mayúsculas y sin espacios al principio o al final

        #Si la entrada es R llamamos a la función main, la cual se ejecutará y mostrará el menú principal
        if (input1=="R"):
            main()

        #Si la entrada es C, continuamos al siguiente paso
        if (input1=="1"):
            print("-------------------------------------------------------------------")
            print("Introduce el número de clase del alumno para leer su información\n")

            #Pedimos por consola el número del alumno que queremos leer
            while True:
                num_alumno=input()

                #Probamos a cambiar el valor introducido a un entero, si devuelve 'ValueError' 
                #sabemos que el valor introducido no era entero y volvemos a pedir una entrada
                try:
                    num_alumno=int(num_alumno)

                except ValueError:
                    print("Entrada inválida, introduce un número")
                    continue #El continue nos devuelve al principio del while True en caso de no poder convertir el valor a entero
                
                #comprobamos que el número introducido exista en el diccionario global de alumnos, si no existe volvemos a preguntar
                if (num_alumno in dict_alumnos_local):
                    
                    #creamos un diccionario que contenga unicamente la información del alumno seleccionado
                    alumno_seleccionado = dict_alumnos_local[num_alumno]

                    #Imprimimos la información asociada a ese número de clase contenida en el nuevo diccionario personal
                    print("\n-------------------------------------------------------------------")
                    print(f"Número de clase del alumno: {alumno_seleccionado["número"]}")
                    print(f"Nombre del alumno: {alumno_seleccionado["nombre"]}")
                    print(f"Apellido del alumno: {alumno_seleccionado["apellido"]}")
                    print(f"Lista de notas del alumno: {alumno_seleccionado["notas"]}")
                    print("-------------------------------------------------------------------")
                    
                    print("R para volver al menú principal\nPulse cualquier tecla para leer la información de otro alumno")
                    while True:
                        if (input().upper().strip()=="R"):
                            main()
                        else: 
                            leer_alumnos(dict_alumnos_local)
                else:
                    print("El número de clase introducido no existe\nVuelve a introducir un número de clase\n")
        if (input=="2"):
            #Bucle for para recorrer los valores del diccionario
            #las claves del diccionario local de alumnos recorren 
            #los valores del diccionario global para imprimir todos los alumnos
            for dict_alumnos_local in dict_alumnos.values(): 
                        #imprimimos el valor asociado a cada clave
                print("\n-------------------------------------------------------------------")
                print(f"Número de clase del alumno: {dict_alumnos_local["número"]}")
                print(f"Nombre del alumno: {dict_alumnos_local["nombre"]}")
                print(f"Apellido del alumno: {dict_alumnos_local["apellido"]}")
                print(f"Lista de notas del alumno: {dict_alumnos_local["notas"]}")

        else:
            print("Entrada inválida, introduce el número 1 o 2 para continuar\n o la letra 'R' para volver al menú principal\n")
            

def actualizar_alumno(dict_alumnos_local):
    print("-------------------------------------------------------------------")
    print("Desde este menú podrás actualizar la información de un alumno existente.\n\nDeberás introducir su número de clase\n")
    print("Podrás:\n-> 1.Modificar su nombre\n->2.Modificars u apellido\n-> 3.modificar ambos")
    print("\nIntroduce la letra 'C' si quieres continuar\nSi deseas volver al menú principal ecribe la letra 'R'")
    print("-------------------------------------------------------------------")

    while True:
        input1=input().strip().upper() #modificamos el input para que siempre esté en mayúsculas y sin espacios al principio o al final

        #Si la entrada es R llamamos a la función main, la cual se ejecutará y mostrará el menú principal
        if (input1=="R"):
            main()

        #Si la entrada es C, continuamos al siguiente paso
        if (input1=="C"):

            while True:
                print("introduce el número de clase del alumno que quieres actualizar")
                num_alumno_local =input()

                try:
                    num_alumno_local=int(num_alumno_local)
                except ValueError:
                    print("error, introduce un número")
                    continue

                if (num_alumno_local in dict_alumnos_local):
                    print(f"alumno seleccionado: {num_alumno_local}")
                    
                    #creamos un diccionario que contenga unicamente la información del alumno seleccionado
                    alumno_seleccionado = dict_alumnos_local[num_alumno_local]

                    #Imprimimos la información asociada a ese número de clase contenida en el nuevo diccionario personal
                    print("\n-------------------------------------------------------------------")
                    print(f"Número de clase del alumno: {alumno_seleccionado["número"]}")
                    print(f"Nombre del alumno: {alumno_seleccionado["nombre"]}")
                    print(f"Apellido del alumno: {alumno_seleccionado["apellido"]}")
                    print(f"Lista de notas del alumno: {alumno_seleccionado["notas"]}")
                    print("-------------------------------------------------------------------")
                    
                    print("\nIntroduce el número de la operación que desear realizar")
                    print("\n-> 1.Modificar su nombre\n-> 2.Modificar su apellido\n-> 3.modificar ambos")
                    
                    while True:
                        
                        operacion=input()
                        match operacion:
                            case "1":
                                print("introduce su nuevo nombre")
                                nuevo_nombre=input().lower().strip()
                                alumno_seleccionado["nombre"]=nuevo_nombre
                                print("Información actualizada")
                                return alumno_seleccionado
                            case "2":
                                print("introduce su nuevo apellido")
                                nuevo_apellido=input().lower().strip()
                                alumno_seleccionado["apellido"]=nuevo_apellido
                                print("Información actualizada")
                                return alumno_seleccionado
                            case "3":
                                print("introduce su nuevo nombre")
                                nuevo_nombre=input().lower().strip()
                                alumno_seleccionado["nombre"]=nuevo_nombre
                                print("introduce su nuevo apellido")
                                nuevo_apellido=input().lower().strip()
                                alumno_seleccionado["apellido"]=nuevo_apellido
                                print("Información actualizada")
                                return alumno_seleccionado
                            case _:
                                print("introduce una operación válida")
                                continue
                else:
                    print("error, el número de clase introducido no se encuentra en la lista")
                    continue

        else:
            print("Entrada inválida, introduce la letra 'C' para continuar o la letra 'R' para volver al menú principal\n")

def eliminar_alumno():

    print("-------------------------------------------------------------------")
    print("Desde este menú podrás eliminar la información de un nuevo alumno.\n\nDeberás introducir:\n->Su número de clase\n->Su nombre\n->Su apellido\n")
    print("Si deseas continuar escribe 'C'\nSi deseas volver al menú principal ecribe la letra 'R'")
    print("-------------------------------------------------------------------")
    

#PROGRAMA
dict_alumnos = {} #diccionario para almacenar a los alumnos con su numero de clase como claves únicas
#Interfaz del menú principal
def main():

    #Declaración de variables:
    int_numero_clase = 0 #Actúa como identificador único (tipo int)
    str_nombre_alumno = ""  #tipo string
    str_apellido_alumno = "" #tipo string
    
    

    print("-------------------------------------------------------------------")
    print("Bienvenido al sistema de gestión de alumnos\n")
    print("Escribe el número de las operación quieres realizar:\n")
    print("-> 1. CREAR ALUMNO\n-> 2. LEER ALUMNO\n-> 3. ACTUALIZAR ALUMNO\n-> 4. ELIMINAR ALUMNO\n")
    print("-------------------------------------------------------------------")

    #Definir los inputs validos en una lista
    lista_inputs_validos = ["1","2","3","4"]

    #Pedir por consola el menú al que quiere acceder
    while True: #pedimos el input mínimo 1 vez, si no coincide con una opción válida, volvemos a pedir un input hasta que sea un número del 1 al 4
        input_menu=input()

        if input_menu in lista_inputs_validos: #si el input es válido se ejecuta el siguiente match-case
            match input_menu:
                case "1":
                    print(f"\nHas seleccionado {input_menu}.CREAR ALUMNO") #input == 1 output: Has seleccionado 1.CREAR ALUMNO
                    
                    crear_alumno(int_numero_clase,str_nombre_alumno,str_apellido_alumno,dict_alumnos)  #llamamos a la función crear_alumno
                    main() #llamada recursiva para volver al menú principal
                case "2":
                    print(f"\nHas seleccionado {input_menu}.LEER ALUMNO\n") #input == 2 output: Has seleccionado 2.LEER ALUMNO
                    print(f"{leer_alumnos(dict_alumnos)}") #llamamos a la función leer_alumnos
                case "3":
                    print(f"\nHas seleccionado {input_menu}.ACTUALIZAR ALUMNO\n") #input == 3 output: Has seleccionado 3.ACTUALIZAR ALUMNO
                    actualizar_alumno(dict_alumnos) #llamamos a la función actualizar_alumno
                    main() #llamada recursiva para volver al menú principal
                    
                case "4":
                    print(f"\nHas seleccionado {input_menu}.ELIMINAR ALUMNO\n") #input == 4 output: Has seleccionado 4.ELIMINAR ALUMNO
                    eliminar_alumno() #llamamos a la función eliminar_alumno
            break #Salimos del bucle para no pedir el input otra vez una vez sea válido
        else:
            print("Opción inválida, escribe un número del 1 al 4\n")

if __name__ == "__main__":
    main()
