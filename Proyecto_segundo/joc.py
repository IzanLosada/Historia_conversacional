from inventari import Inventari

def iniciar_partida(zona_inicial):
    print("\n==================================================")
    print("      INICIALITZANT SISTEMA DE LA NAU...          ")
    print("==================================================")
    print("Any 2120 D.C. - Has despertat del son d'hivernació.")
    print("Benvingut a bord, capità Bond.\n")
    
    zona_actual = zona_inicial
    inventari_jugador = Inventari()
    jugant = True

    while jugant:
        print(f"\n[ Zona actual: {zona_actual.nom} ]")
        zona_actual.mostrar_descripcio()
        
        print("\nSortides disponibles:")
        if zona_actual.sortides:
            for sortida in zona_actual.sortides:
                print(f" - {sortida.nom}")
        else:
            print("Cap sortida visible.")
        
        if zona_actual.objectes:
            print("\nObjectes a la zona:")
            for obj in zona_actual.objectes:
                print(f" - {obj.nom}: {obj.descripcio}")

        print("\nInventari:", end=" ")
        if inventari_jugador.objectes:
            noms_inventari = [obj.nom for obj in inventari_jugador.objectes]
            print(", ".join(noms_inventari))
        else:
            print("Buit")

        text_usuari = input("\n> ").strip().lower()
        
        if text_usuari in ["sortir", "exit", "tornar"]:
            print("\nTornant al menú principal...")
            jugant = False
            continue

        paraules = text_usuari.split()

        if len(paraules) > 2:
            print("\nMàxim de dues paraules permeses.")
            continue

        if len(paraules) == 1:
            desti_trobat = None
            for sortida in zona_actual.sortides:
                if sortida.nom.lower() == paraules[0]:
                    desti_trobat = sortida
                    break
            
            if desti_trobat:
                zona_actual = desti_trobat
                print(f"\nT'has mogut a: {zona_actual.nom}")
            else:
                print("\nAcció o zona no reconeguda.")

        elif len(paraules) == 2:
            accio = paraules[0]
            objectiu = paraules[1]

            if accio == "agafar":
                obj_trobat = None
                for obj in zona_actual.objectes:
                    if objectiu in obj.nom.lower():
                        obj_trobat = obj
                        break
                
                if obj_trobat:
                    zona_actual.eliminar_objecte(obj_trobat)
                    inventari_jugador.afegir_objecte(obj_trobat)
                    print(f"\nHas agafat: {obj_trobat.nom}")
                else:
                    print(f"\nNo hi ha cap objecte anomenat '{objectiu}' aquí.")
            else:
                print(f"\nAcció '{accio}' no reconeguda.")