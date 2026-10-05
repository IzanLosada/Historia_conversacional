from inventari import Inventari
from ihall import IHall

def iniciar_partida(zona_inicial, llista_zones_instancia, malien_instancia):
    print("\n==================================================")
    print("      INICIALITZANT SISTEMA DE LA NAU...          ")
    print("==================================================")
    print("Any 2120 D.C. - Has despertat del son d'hivernació.")
    print("Benvingut a bord, capità Bond.\n")
    
    zona_actual = zona_inicial
    inventari_jugador = Inventari()
    jugant = True
    llanterna_encesa = False
    ihall = IHall()

    totes_habitacions = [z.nom for z in llista_zones_instancia]
    
    llanterna_usada_tallers = False
    zona_anterior = zona_actual

    while jugant:
        if zona_anterior.nom.lower() == "tallers" and zona_actual.nom.lower() != "tallers" and llanterna_usada_tallers:
            print("\n[Avís del sistema]: S'ha trencat la llanterna o s'ha fos en sortir dels tallers a causa de l'ús intensiu!")
            llanterna_usada_tallers = False

        zona_anterior = zona_actual

        ubicacio_actual_llanterna = "en possessió del jugador o desconeguda"
        for zona in llista_zones_instancia:
            for obj in zona.objectes:
                if "llanterna" in obj.nom.lower():
                    ubicacio_actual_llanterna = zona.nom
                    break

        context_joc = {
            "ubicacio_llanterna": ubicacio_actual_llanterna,
            "totes_habitacions": totes_habitacions,
            "ubicacio_malien": malien_instancia.zona_actual.nom
        }

        ihall.interaccio_torn(context_joc)

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

        if len(paraules) == 1:
            desti_trobat = None
            for sortida in zona_actual.sortides:
                if sortida.nom.lower() == paraules[0]:
                    desti_trobat = sortida
                    break
            
            if desti_trobat:
                zona_actual = desti_trobat
                print(f"\nT'has mogut a: {zona_actual.nom}")
                malien_instancia.moure_aleatoriament()
                if not malien_instancia.verificar_trobada(type('ObjJugador', (), {'zona_actual': zona_actual, 'inventari': inventari_jugador})()):
                    jugant = False
            else:
                print("\nAcció o zona no reconeguda.")

        else:
            accio = paraules[0]
            objectiu = " ".join(paraules[1:])

            if accio == "agafar":
                if zona_actual.nom.lower() == "tallers" and "eina" in objectiu:
                    te_llanterna_inv = any("llanterna" in obj.nom.lower() for obj in inventari_jugador.objectes)
                    if not te_llanterna_inv or not llanterna_encesa:
                        print("\nEstà massa fosc per agafar l'eina.")
                        continue

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

            elif accio in ["utilitzar", "encendre"]:
                obj_trobat = None
                for obj in inventari_jugador.objectes:
                    if objectiu in obj.nom.lower():
                        obj_trobat = obj
                        break
                
                if not obj_trobat:
                    print(f"\nNo tens l'objecte '{objectiu}' al teu inventari.")
                    continue

                if "llanterna" in objectiu.lower():
                    llanterna_encesa = True
                    print("\nHas utilitzat la llanterna. Ara pots veure-hi clarament.")
                    if zona_actual.nom.lower() == "tallers":
                        llanterna_usada_tallers = True
                    
                    inventari_jugador.eliminar_objecte(obj_trobat)
                    print("La llanterna s'ha trencat (només tenia un ús) i l'has perdut de l'inventari.")

                elif "eina" in objectiu.lower() and zona_actual.nom.lower() == "propulsors":
                    print("\nHas utilitzat l'eina als propulsors. Motor reparat correctament!")
                else:
                    print(f"\nNo pots utilitzar '{objectiu}' aquí.")
            
            else:
                print(f"\nAcció '{accio}' no reconeguda.")