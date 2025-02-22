import string

'''
- title: practica bucle for
- author: luis.polanco
- date: 02.17.2025 
'''

def programa():
    # Texto de ejemplo
    texto = """
    Python es un lenguaje de programación poderoso y versátil. Python se usa en desarrollo web, 
    inteligencia artificial, ciencia de datos, automatización y mucho más. Python es fácil de aprender y 
    tiene una gran comunidad de desarrolladores.
    """

    # Paso 1: Normalizar el texto
    texto = texto.lower()  # Convertir a minúsculas
    texto = texto.translate(str.maketrans("", "", string.punctuation))  # Eliminar puntuación

    # Paso 2: Dividir el texto en palabras
    palabras = texto.split()

    # -------------
    # # Solución I - Algoritmo de complejidad exponencial
    # -------------
    # Inicializamos una variable para llevar el máximo de frecuencia
    max_frecuencia = 0
    palabra_max_frecuencia = ""

    # Recorremos cada palabra del array
    for palabra in palabras:
        frecuencia_actual = 0
        # Contamos cuántas veces aparece 'palabra' en el array
        for palabra_actual_analizada in palabras:
            if  palabra_actual_analizada == palabra:
                frecuencia_actual += 1
            # Actualizamos la frecuencia máxima si corresponde
        if frecuencia_actual > max_frecuencia:
            max_frecuencia = frecuencia_actual
            palabra_max_frecuencia = palabra_actual_analizada

    print(f"la palabra de max frecuencia es {palabra_max_frecuencia} con {max_frecuencia} veces")

    # -------------
    # # Solución II - Algoritmo de complejidad lineal
    # -------------
    # Contar la frecuencia de cada palabra usando un diccionario
    frecuencia_palabras = {}
    for palabra in palabras:
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] += 1  # Sumar 1 si la palabra ya existe
        else:
            frecuencia_palabras[palabra] = 1  # Agregar la palabra al diccionario

    max_frecuencia = 0
    max_palabra = ""
    for palabra, frecuencia in frecuencia_palabras.items():
        if(frecuencia > max_frecuencia):
            max_frecuencia = frecuencia
            max_palabra = palabra
    
    print(f"la palabra de max frecuencia es {max_palabra} con {max_frecuencia} veces")

    # -------------
    # Solución III - Buscamos el máximo haciendo uso de la función max()
    # -------------
     # Paso 4: Encontrar la palabra más frecuente
    palabra_mas_frecuente = max(frecuencia_palabras, key=frecuencia_palabras.get)
    max_frecuencia = frecuencia_palabras[palabra_mas_frecuente]

    # Paso 5: Mostrar los resultados
    print("\n🔹 **Frecuencia de palabras en el texto:**")
    for palabra, frecuencia in frecuencia_palabras.items():
        print(f"{palabra}: {frecuencia}")

    print(f"\n **La palabra más frecuente es:** '{palabra_mas_frecuente}' con {max_frecuencia} apariciones")


    # Paso 6: Mostrar los resultados de forma ordenada descendente
    print("\n **Frecuencia de palabras en el texto:**")
    for palabra, frecuencia in sorted(frecuencia_palabras.items(), key=lambda x: x[1], reverse=True):
        print(f"{palabra}: {frecuencia}")

    print(f"\n🔹 **La palabra más frecuente es:** '{palabra_mas_frecuente}' con {max_frecuencia} apariciones")

# Bloque principal para ejecutar la práctica
if __name__ == "__main__":
    programa()