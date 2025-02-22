#PRÁCTICA BUCLE FOR:
#1. recibir un texto en forma de cadena
#2.se elimina la puntuación y se convierte todo a minusculas
#3.se separa en palabras y se cuenta la frecuencia
#4. se muestra un resumen con la palabras mas comunes

#LIBRERIAS
import string

def programa():
    #texto placeholder
    texto ="""
    python es un lenguaje de programación poderoso y versátil. Python se usa en desarollo web, inteligencia artificial
    , ciencia de datos, automatización y mucho más. python es fácil de aprender u tiene una gran comunidad de desarrolladores
    """
    #paso 1
    #sobreescribimos la variable original y convertimos el texto a minúsculas
    texto = texto.lower()
    #sustituimos los signos de puntuación por espacios blancos
    texto = texto.translate(str.maketrans("","", string.punctuation))

    print(texto)


    #paso 2
    #separamos las palabras y las guardamos en un array 
    palabras = texto.split()

    print(texto)

    #contar la frecuencia
    """"
    for palabra in palabras:
        frecuencia_actual=0
        #contamos cuantas veces aparece 'palabra' en el string
        for palabra_actual_analizada in palabras:
            if palabra_actual_analizada == palabras:
                frecuencia_actual += 1
                
                #actualizamos la frecuencia máxima si corresponde
        if frecuencia_actual > max_frecuencia:
            max_frecuencia = frecuencia_actual
            palabra_max_frecuencia = palabra_actual_analizada

    print(palabra_max_frecuencia) #POCO EFICIENTE
    """
    
    #contar la frecuencia (complejidad algoritmica lineal)
    frecuencia_palabras = {}
    for palabra in palabras:
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] += 1 #sumar 1 si la palabra se encuentra en el diccionario

        else:
            frecuencia_palabras[palabra] =1 #agregar la palabra al diccionario
    

    max_frecuencia = 0
    max_palabra = ""
    for palabra, frecuencia in frecuencia_palabras.items():
        if(frecuencia > max_frecuencia):
            max_frecuencia = frecuencia
            max_palabra = palabra

    print(f"palabra: {max_palabra} frecuencia: {max_frecuencia}")

    #usando max()

    palabra_mas_frecuente = max(frecuencia_palabras, key=frecuencia_palabras.get())
    max_frecuencia = frecuencia_palabras[palabra_mas_frecuente]

    print("\n **Frecuencia de palabras en el texto:**")
    for palabra, frecuencia in sorted(frecuencia_palabras.items(), key=lambda x: x[1], reverse=True):
        print(f"{palabra}")

if __name__ == "__main__":
    programa()