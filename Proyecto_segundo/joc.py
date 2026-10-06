from inventari import Inventari
from ihall import IHall
from objecte import llanterna, eina

ZONES_RESTRINGIDES = ["comandament", "sala sortida exterior"]


def buscar(objectes, text):
    """Retorna el primer objecte el nom del qual conté 'text' (o None)."""
    if not text:
        return None
    return next((o for o in objectes if text in o.nom.lower()), None)


def iniciar_partida(zona_inicial, zones, malien):
    print("==================================================")
    print("      INICIALITZANT SISTEMA DE LA NAU...          ")
    print("==================================================")
    print("Any 2120 D.C. - Has despertat del son d'hivernació.")
    print("Benvingut a bord, capità Bond.")

    zona = zona_inicial
    inventari = Inventari()
    ihall = IHall()
    llanterna_encesa = False
    noms_zones = [z.nom for z in zones]
    jugant = True

    while jugant:
        ubicacio_llanterna = next(
            (z.nom for z in zones if buscar(z.objectes, "llanterna")),
            "en possessió del jugador o desconeguda"
        )
        ihall.interaccio_torn({
            "ubicacio_llanterna": ubicacio_llanterna,
            "totes_habitacions": noms_zones,
            "ubicacio_malien": malien.zona_actual.nom
        })

        print(f"[ Zona actual: {zona.nom} ]")
        zona.mostrar_descripcio()

        print("Sortides disponibles:")
        if zona.sortides:
            for sortida in zona.sortides:
                print(f" - {sortida.nom}")
        else:
            print("Cap sortida visible.")

        if zona.objectes:
            print("Objectes a la zona:")
            for obj in zona.objectes:
                print(f" - {obj.nom}: {obj.descripcio}")

        noms_inventari = ", ".join(o.nom for o in inventari.objectes)
        print("Inventari:", noms_inventari or "Buit")

        text_usuari = input("\n> ").strip().lower()

        if text_usuari in ["sortir", "exit", "tornar"]:
            print("Tornant al menú principal...")
            break

        paraules = text_usuari.split()
        if not paraules:
            continue

        accio = paraules[0]
        objectiu = " ".join(paraules[1:])

        if accio == "anar":
            if not objectiu:
                print("A quina zona vols anar? Revisa les sortides disponibles.")
                continue

            desti = next((s for s in zona.sortides if s.nom.lower() == objectiu), None)
            if not desti:
                print(f"No hi ha cap sortida directa cap a '{objectiu}'.")
                continue

            nom_desti = desti.nom.lower()

            if nom_desti in ZONES_RESTRINGIDES and not buscar(inventari.objectes, "targeta identificadora"):
                print("Accés denegat! Aquesta zona requereix la 'Targeta identificadora' per obrir la porta de seguretat.")
                continue

            if nom_desti == "propulsors" and not buscar(inventari.objectes, "vestit"):
                print("==================================================")
                print("     GAME OVER - ASFIXIA A L'ESPAI EXTERIOR       ")
                print("==================================================")
                print("Has sortit als propulsors sense el vestit espacial!")
                print("T'has quedat sense oxigen i has mort a l'espai buit.")
                break

            # La llanterna es trenca en sortir dels tallers si està encesa
            if zona.nom.lower() == "tallers" and llanterna_encesa:
                llanterna_encesa = False
                l = buscar(inventari.objectes, "llanterna")
                if l:
                    inventari.eliminar_objecte(l)
                print("[Avís del sistema]: S'ha trencat la llanterna en sortir dels tallers a causa de l'ús intensiu!")

            zona = desti
            print(f"T'has mogut a: {zona.nom}")

            malien.moure_aleatoriament()
            if not malien.verificar_trobada(zona, inventari):
                break

        elif accio in ["obrir", "escorcollar", "buscar"] and "escriptori" in objectiu:
            escriptori = buscar(zona.objectes, "escriptori")
            if not escriptori:
                print("No hi ha cap escriptori en aquesta zona.")
            elif escriptori.revisat:
                print("Ja has escorcollat l'escriptori i no hi ha res més a dins.")
            else:
                escriptori.revisat = True
                if escriptori.contingut:
                    print("Has obert els calaixos de l'escriptori i has trobat:")
                    for obj in escriptori.contingut:
                        zona.afegir_objecte(obj)
                        print(f" - {obj.nom}")
                    escriptori.contingut = []
                else:
                    print("L'escriptori està buit.")

        elif accio == "agafar":
            obj = buscar(zona.objectes, objectiu)
            if not obj:
                print(f"No hi ha cap objecte anomenat '{objectiu}' aquí.")
            elif not obj.portable:
                print(f"No pots agafar {obj.nom.lower()}, és massa gran.")
            elif obj is eina and zona.nom.lower() == "tallers" and not llanterna_encesa:
                print("Està massa fosc per agafar l'eina.")
            else:
                zona.eliminar_objecte(obj)
                inventari.afegir_objecte(obj)
                print(f"Has agafat: {obj.nom}")

        elif accio == "deixar":
            obj = buscar(inventari.objectes, objectiu)
            if obj:
                inventari.eliminar_objecte(obj)
                zona.afegir_objecte(obj)
                print(f"Has deixat: {obj.nom} a {zona.nom}")
            else:
                print(f"No tens cap objecte anomenat '{objectiu}' al teu inventari.")

        elif accio in ["utilitzar", "encendre"]:
            obj = buscar(inventari.objectes, objectiu)
            if not obj:
                print(f"No tens l'objecte '{objectiu}' al teu inventari.")
            elif obj is llanterna:
                if llanterna_encesa:
                    print("La llanterna ja està encesa.")
                else:
                    llanterna_encesa = True
                    print("Has encès la llanterna. Ara pots veure-hi clarament.")
            elif obj is eina and zona.nom.lower() == "propulsors":
                print("==================================================")
                print("        VICTÒRIA! HAS REPARAT LA NAU              ")
                print("==================================================")
                print("Has utilitzat l'eina als propulsors amb èxit.")
                print("Els motors principals s'han tornat a encendre.")
                print("Felicitats, capità Bond! Has salvat la nau i completat la missió.")
                break
            else:
                print(f"No pots utilitzar '{objectiu}' aquí.")

        else:
            print("Comanda no reconeguda. Intenta 'anar <zona>', 'agafar', 'deixar', 'obrir' o 'utilitzar'.")