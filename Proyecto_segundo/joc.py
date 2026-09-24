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

        text_usuari = input("\nOn vols anar? (o escriu 'sortir' per tornar al menú) > ").lower()
        
        if text_usuari in ["sortir", "exit", "tornar"]:
            print("\nTornant al menú principal...")
            jugant = False
            continue

        zona_desti_trobada = None
        for sortida in zona_actual.sortides:
            if sortida.nom.lower() == text_usuari:
                zona_desti_trobada = sortida
                break
        
        if zona_desti_trobada:
            zona_actual = zona_desti_trobada
            print(f"\nT'has mogut correctament a: {zona_actual.nom}")
        else:
            print("\nNo pots anar a aquesta zona directament des d'aquí o el nom no és correcte.")