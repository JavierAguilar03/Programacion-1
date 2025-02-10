#ejemplo de práctica con tipos primitivos y diccionarios en Python

#1. solicitar datos al usuario (cadena, entero, flotante y booleano)

texto = input("ingresa un texto")
entero_txt = input("ingresa un entero")

entero_int = int(entero_txt) #(conversión de tipos explícita) convertimos la cadena a entero

flotante_txt= input("ingresa un número flotante")
flotante_float = float(flotante_txt) #conversión a flotante

booleano_txt = input("ingresa 'True' o 'False': ")
booleano_bool =(booleano_txt == "True") #Se convierte a booleano solamente si la cadena es 'True'

#crear un diccionario
mi_diccionario = {
    "kTexto": texto,
    "kEntero_int": entero_int,
    "kEntero_txt": entero_txt,
    "kFlotante_float": flotante_float,
    "kFlotante_txt": flotante_txt,
    "kBooleano_bool": booleano_bool,
    "kBooleano_txt": booleano_txt
}


print(texto)
print(str(entero_int)) #convertir a cadena para el print (el print espera imprimir cadenas)
print(flotante_float)
print(booleano_bool)

print("entero: " + str(entero_int) +",flotante: "+str(flotante_float) + ", booleano: " + str(booleano_bool)) #convertir tipos a str para concatenar

#imprimir el diccionario
print("\nDiccionario creado: ")
print(mi_diccionario)

#modificar uno de los valores en el diccionario
mi_diccionario["kentero_int"] = 999
## mi_diccionario("kentero_int") = "999" ERROR no guardar tipo texto en una variable hecha para enteros