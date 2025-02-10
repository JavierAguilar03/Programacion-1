# CREAR UNA CALCULADORA QUE PERMITA LAS OPERACIONES: +,-,*,/
print("--------------------------------")
print("Bienvenido a la calculadora")
print("--------------------------------")

#inicializar las variables globales para los números y el operador
fl_num_1= 0.0 #primer número (tipo:float)
fl_num_2 = 0.0 #segundo número (tipo:float)
str_operador=None #operador (tipo:string)

#función para realizar el cálculo con los parametros dados
def calculadora(fl_num_1_local, fl_num_2_local, str_operador_local):

    #inicializar variable resultado a 0
    resultado=0

    #comprobar el valor del operador y almacenar el valor que devuelve
    match str_operador:
        case '+':
            resultado=fl_num_1_local+fl_num_2_local
            return resultado
        case '-':
            resultado=fl_num_1_local-fl_num_2_local
            return resultado
        case '*':
            resultado=fl_num_1_local*fl_num_2_local
            return resultado
        case '/':
            resultado=fl_num_1_local/fl_num_2_local
            if(fl_num_2_local) == 0:
                print("error: división entre 0")
            return resultado
        

#pedir input de los números y el operador, forzando sus tipos (numeros: float, operador:str)
# y
#control de errores de tipo

while(True):
    
    print("introduce la operación que quieres realizar")
    print("Operaciones válidas:")
    print("+")
    print("-")
    print("*")
    print("/")
    print("escribe exit para salir de la calculadora")
    print("--------------------------------")
    str_operador=str(input()) #definir el tipo del input para el operador como string
    if str_operador not in ("+","-","*","/","exit"):
        print("--------------------------------")
        print("ERROR, introduce valores válidos")
        print("--------------------------------")
        continue #si no se introduce un valor válido vuelve al principio del bucle
    
    #salir del bucle si el input es exit
    if (str_operador=="exit"):
        print("saliendo de la calculadora ...")
        break

    #comprobar que la consola no devuelve un error tipo ValueError
    #si no devuelve error pedir los números
    try:
        print("introduce el primer numero")
        print("--------------------------------")
        fl_num_1=float(input()) #definir el tipo del input para el primer número como float
        print("introduce el segundo numero")
        print("--------------------------------")
        fl_num_2=float(input()) #definir el tipo del input para el segundo número como float
    except ValueError:
        print("--------------------------------")
        print("ERROR, introduce valores válidos")
        print("--------------------------------")
        continue #volver al principio del bucle

    #imprimir la operación llamando a la función calculadora
    print("\n--------------------------------\n")                    
    print(f"Operación realizada: {fl_num_1} {str_operador} {fl_num_2} = {calculadora(fl_num_1, fl_num_2, str_operador)}")
    print("\n--------------------------------\n")



