import re  # Para validar la contraseña con expresiones regulares

def validar_contraseña(contraseña):
    """
    Verifica si la contraseña cumple con los requisitos:
    - Al menos 8 caracteres
    - Contiene una letra mayúscula, una minúscula y un número
    """
    if len(contraseña) < 8:
        print("❌ Error: La contraseña debe tener al menos 8 caracteres.")
        return False
    if not re.search(r"[A-Z]", contraseña):
        print("❌ Error: La contraseña debe contener al menos una letra mayúscula.")
        return False
    if not re.search(r"[a-z]", contraseña):
        print("❌ Error: La contraseña debe contener al menos una letra minúscula.")
        return False
    if not re.search(r"[0-9]", contraseña):
        print("❌ Error: La contraseña debe contener al menos un número.")
        return False
    return True

def registrar_contraseña():
    """
    Permite al usuario registrar una nueva contraseña válida.
    """
    while True:
        contraseña = input("🔑 Crea una nueva contraseña: ")
        if validar_contraseña(contraseña):
            print("✅ Contraseña guardada correctamente.")
            return contraseña  # Se retorna la contraseña válida guardada

def iniciar_sesion(contraseña_guardada):
    """
    Permite al usuario iniciar sesión verificando la contraseña.
    Tiene un límite de 3 intentos.
    """
    intentos = 3
    while intentos > 0:
        intento = input("🔑 Introduce tu contraseña: ")
        if intento == contraseña_guardada:
            print("✅ Inicio de sesión exitoso.")
            return True
        else:
            intentos -= 1
            print(f"❌ Contraseña incorrecta. Intentos restantes: {intentos}")

    print("🚫 Demasiados intentos fallidos. Acceso bloqueado.")
    return False

def menu():
    """
    Menú principal del sistema de gestión de contraseñas.
    """
    contraseña_guardada = None  # No hay contraseña al inicio

    while True:
        print("\n--- SISTEMA DE GESTIÓN DE CONTRASEÑAS ---")
        print("1. Registrar nueva contraseña")
        print("2. Iniciar sesión")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            contraseña_guardada = registrar_contraseña()
        elif opcion == "2":
            if contraseña_guardada is None:
                print("⚠️ No hay ninguna contraseña registrada. Regístrate primero.")
            else:
                if iniciar_sesion(contraseña_guardada):
                    print("🔓 Bienvenido al sistema.")
        elif opcion == "3":
            print("👋 Saliendo del programa...")
            break
        else:
            print("❌ Opción inválida. Inténtalo de nuevo.")


# Ejecutar el programa
if __name__ == "__main__":
    menu()
