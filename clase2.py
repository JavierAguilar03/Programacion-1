# Pedir por linea de comando un día de la semana y haciendo uso de un bucle if (parte 1) y match case (parte 2) 
# decir si es fin de semana o entre semana

#pedir un dia de la semana por linea de comando
print("input día de la semana")

#inicializar variables
dia_semana=None

#pido el dia de la semana
dia_semana = input()

#creo un array con todos lo días de la semana
dias=["lunes","martes","miércoles","jueves","viernes","sábado","domingo"]

#comprobar que el texto sin espacios y en minusculas coincide con un valor del array dias[]
while(dia_semana.strip().lower() not in dias):
    print("input día de la semana")
    dia_semana = input()
    
    """"
    #parte 1: if else
    def semana_if():
        if(dia_semana=="sábado"):
            return "fin de semana"
        elif(dia_semana=="domingo"):
            return "fin de semana"
        else:
            return "entre semana"
    print(semana_if())
    """
    #parte 2: match-case
    def semana_match():
        match dia_semana:
            case "lunes":
                return "entre semana"
            case "martes":
                return "entre semana"
            case "miércoles":
                return "entre semana"
            case "jueves":
                return "entre semana"
            case "viernes":
                return "entre semana"
            case "sábado":
                return "fin de semana"
            case "domingo":
                return "fin de semana"
    print(semana_match())