from inventari import Inventari
from ihall import IHall

class JugadorEstat:
    def __init__(self, zona_actual, inventari):
        self.zona_actual = zona_actual
        self.inventari = inventari

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

        accio = paraules[0]
        if len(paraules) > 1:
            objectiu = " ".join(paraules[1:])
        else:
            objectiu = ""

        if accio == "anar":
            if not objectiu:
                print("\nA quina zona vols anar? Revisa les sortides disponibles.")
                continue

            desti_trobat = None
            for sortida in zona_actual.sortides:
                if sortida.nom.lower() == objectiu.lower():
                    desti_trobat = sortida
                    break
            
            if desti_trobat: # Buscamos targeta en inventario del jugador
                te_targeta = any("targeta identificadora" in obj.nom.lower() for obj in inventari_jugador.objectes)
                zones_restringides = ["comandament", "sala sortida exterior"]

                if desti_trobat.nom.lower() in zones_restringides and not te_targeta:
                    print("\nAccés denegat! Aquesta zona requereix la 'targeta_identificadora' per obrir la porta de seguretat.")
                    continue

                if desti_trobat.nom.lower() == "propulsors":
                    te_vestit = any("vestit_espacial" in obj.nom.lower() or "vestit" in obj.nom.lower() for obj in inventari_jugador.objectes)
                    if not te_vestit:
                        print("\n==================================================")
                        print("     GAME OVER - ASFIXIA A L'ESPAI EXTERIOR       ")
                        print("==================================================")
                        print("Has sortit als propulsors sense el vestit espacial!")
                        print("T'has quedat sense oxigen i has mort a l'espai buit.")
                        jugant = False
                        continue

                zona_actual = desti_trobat
                print(f"\nT'has mogut a: {zona_actual.nom}")
                
                malien_instancia.moure_aleatoriament()
                jugador_estat = JugadorEstat(zona_actual, inventari_jugador)
                if not malien_instancia.verificar_trobada(jugador_estat):
                    jugant = False
            else:
                print(f"\nNo hi ha cap sortida directa cap a '{objectiu}'.")

        elif accio in ["obrir", "escorcollar", "buscar"] and "escriptori" in objectiu:
            escriptori_trobat = None
            for obj in zona_actual.objectes:
                if "escriptori" in obj.nom.lower():
                    escriptori_trobat = obj
                    break
            
            if escriptori_trobat:
                if not escriptori_trobat.revisat:
                    escriptori_trobat.revisat = True
                    if escriptori_trobat.contingut:
                        print("\nHas obert els calaixos de l'escriptori i has trobat:")
                        for obj in list(escriptori_trobat.contingut):
                            zona_actual.afegir_objecte(obj)
                            print(f" - {obj.nom}")
                        escriptori_trobat.contingut = []
                    else:
                        print("\nL'escriptori està buit.")
                else:
                    print("\nJa has escorcollat l'escriptori i no hi ha res més a dins.")
            else:
                print("\nNo hi ha cap escriptori en aquesta zona.")

        elif accio == "agafar":
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
                if obj_trobat.nom.lower() == "escriptori":
                    print("\nNo pots agafar l'escriptori, és massa gran.")
                    continue

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
                print("\n==================================================")
                print("        VICTÒRIA! HAS REPARAT LA NAU              ")
                print("==================================================")
                print("Has utilitzat l'eina als propulsors amb èxit.")
                print("Els motors principals s'han tornat a encendre.")
                print("Felicitats, capità Bond! Has salvat la nau i completat la missió.")
                jugant = False

            else:
                print(f"\nNo pots utilitzar '{objectiu}' aquí.")
        
        else:
            print(f"\nComanda no reconeguda. Intenta 'anar <zona>', 'agafar', 'deixar', 'obrir' o 'utilitzar'.")