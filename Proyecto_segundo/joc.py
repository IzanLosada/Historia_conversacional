from inventari import Inventari

def iniciar_partida(zona_inicial):
    print("\n=== NAU PIAXXII: HISTÒRIA CONVERSACIONAL ===")
    print("Any 2120 D.C. - Despertant del son induït...\n")
    
    zona_actual = zona_inicial
    inventari_jugador = Inventari()
    jugant = True

    while jugant:
        print(f"\n--- {zona_actual.nom} ---")
        zona_actual.mostrar_descripcio()
        zona_actual.mostrar_sortides()
        
        if zona_actual.objectes:
            print("Objectes a la zona:")
            for obj in zona_actual.objectes:
                print(f" - {obj.nom}: {obj.descripcio}")

        text_usuari = input("\nQuè vols fer? > ").strip().lower()
        
        if text_usuari in ["sortir", "exit", "tornar"]:
            print("Tornant al menú principal...")
            jugant = False
            continue

        parts = text_usuari.split(" ", 1)
        verb = parts[0]
        destinacio_nom = parts[1] if len(parts) > 1 else text_usuari

        if verb == "anar" or len(parts) == 1:
            zona_desti_trobada = next((s for s in zona_actual.sortides if s.nom.lower() == destinacio_nom), None)
            if zona_desti_trobada:
                zona_actual = zona_desti_trobada
                print(f"T'has mogut a {zona_actual.nom}.")
            else:
                print("No pots anar a aquesta zona directament des d'aquí.")
        else:
            print(f"Acció '{verb}' no reconeguda encara.")