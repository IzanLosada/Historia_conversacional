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
    llanterna_encesa = False  # Estat inicial de la llanterna

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
        if not paraules:
            continue

        # Si només s'escriu una paraula, comprovem si és per moure's
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

        else:
            # Si té 2 o més paraules: la primera és l'acció, la resta l'objectiu
            accio = paraules[0]
            objectiu = " ".join(paraules[1:])

            # --- ACCIÓ: AGAFAR ---
            if accio == "agafar":
                # Comprovació de zona fosca (Tallers)
                if zona_actual.nom.lower() == "tallers" and "eina" in objectiu:
                    te_llanterna = False
                    for obj in inventari_jugador.objectes:
                        if "llanterna" in obj.nom.lower():
                            te_llanterna = True
                            break
                    
                    # Si no la té o la té però no està encesa
                    if not te_llanterna or not llanterna_encesa:
                        print("\nEstà massa fosc per agafar l'eina.")
                        continue

                # Buscar l'objecte a la zona actual
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

            # --- ACCIÓ: DEIXAR ---
            elif accio == "deixar":
                obj_trobat = None
                for obj in inventari_jugador.objectes:
                    if objectiu in obj.nom.lower():
                        obj_trobat = obj
                        break
                
                if obj_trobat:
                    inventari_jugador.eliminar_objecte(obj_trobat)
                    zona_actual.afegir_objecte(obj_trobat)
                    print(f"\nHas deixat: {obj_trobat.nom} a {zona_actual.nom}")
                else:
                    print(f"\nNo tens cap objecte anomenat '{objectiu}' al teu inventari.")

            # --- ACCIÓ: USAR / ENCENDRE ---
            elif accio in ["usar", "encendre"]:
                te_objecte = False
                for obj in inventari_jugador.objectes:
                    if objectiu in obj.nom.lower():
                        te_objecte = True
                        break
                
                if not te_objecte:
                    print(f"\nNo tens l'objecte '{objectiu}' al teu inventari.")
                    continue

                if "llanterna" in objectiu:
                    llanterna_encesa = True
                    print("\nHas encès la llanterna. Ara pots veure-hi clarament.")
                elif "eina" in objectiu and zona_actual.nom.lower() == "propulsors":
                    print("\nHas utilitzat l'eina als propulsors. Motor reparat correctament!")
                else:
                    print(f"\nNo pots usar '{objectiu}' aquí.")
            
            else:
                print(f"\nAcció '{accio}' no reconeguda.")