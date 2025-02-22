#IMAGINA QUE TIENES UN ARCHIVO DE REGISTROS DE TRANSACCIONES BANCARIAS LLAMADO "transacciones.txt" con el siguiente formato
#UTILIZA UN GENERATOR COMPREHENSION

#Práctica sobre comprehensions y lectura de ficheros

ROOT_PATH = "C:\\Users\\jagui\\OneDrive\\Documentos\\universidad\\2º\\2º Cuatrimestre\\Programación 1\\practica_clase"

def leer_archivo(nombre_archivo):  
    print("[nombre_archivo]------------- START")      #r es el modo de abrir el archivo (modo lectura)/ solo un proceso puede 
                                                      #tener el modo escritura/ 
                                                      #append escribe al final del fichero
    with open(nombre_archivo, "r") as archivo:        #apunta a la linea 0 caracter 0 del fichero
        for linea in archivo:                         #lee linea a linea
            yield linea.strip()                       #eliminar espacios en blanco y saltos de linea | yield: comprehension, solo calcula la linea cuando la llamemos, espera al next       
    print("[nombre_archivo]------------- END")


def programa():
    for linea in leer_archivo(f"{ROOT_PATH}\\transacciones.txt"):
        print(linea)
        
    #generator que filtra solo transacciones "Aprobado"
    transacciones_aprobadas= (
        linea for linea in leer_archivo(f"{ROOT_PATH}\\transacciones.txt") if "Aprobado" in linea
    )
    for transaccion in transacciones_aprobadas:
        print(transaccion)
    
    #mostrar la 5 primeras
    print("[nombre_archivo] MOSTRAR PRIMEROS 4 ------------- START")
    for i, transaccion in enumerate(transacciones_aprobadas):
        print(transaccion)
        if i==4: #solo mostramos las primeras i
            break
    print("[nombre_archivo] MOSTRAR PRIMEROS 4 ------------- END")


    
if __name__ == "__main__":
    programa()