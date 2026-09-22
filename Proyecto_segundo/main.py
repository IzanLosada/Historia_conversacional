print("================================================")
print("        JOC P000 Historia Conversacional        ")
print("================================================")
print()
print("1. Jugar")
print("2. Créditos")
print("3. Crear personatge")
print("4. Salir")
print()

opcio = input("Selecciona una opció: ")

match opcio:
    case 1 :
            print()
            print("¡Comença una partida!")
    case 2:
            print()
            print("CRÉDITOS")
            print("Juego creado por Xinhao")
    case 3:
            print()
            print("Crear Personatge")

    case 4:
            print()
            print("¡Adéu fins aviat!")
            
    case _:
        print("OPCIÓ NO VALIDA ")
    
