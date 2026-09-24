from joc import iniciar_partida
from inventari import Inventari
from objecte import donuts, eina, llanterna, targeta_company, targeta_identificadora, vestit_espacial
from zona import Zona

def inicialitzar_mon():
    tallers = Zona(1, "Tallers", "Zona dels tallers de la nau. Està a les fosques...")
    oficines = Zona(2, "Oficines", "Oficines centrals de la nau. Hi ha escriptoris amb calaixos.")
    banys = Zona(3, "Banys", "Els banys de la nau. Tot aigualit i net.")
    vestuari = Zona(4, "Vestuari", "El vestuari de la nau. Aquí s'guarda l'equipament espacial.")
    comandament = Zona(5, "Comandament", "La sala de comandament de la nau. On es troba l'ordinador iHall.")
    dormitori = Zona(6, "Dormitori", "El dormitori de la nau on el capità Bond s'ha despertat de l'hivernació.")
    cuina = Zona(7, "Cuina", "La cuina de la nau. Olors de menjar sintètic i... dònuts!")
    menjador = Zona(8, "Menjador", "El menjador de la nau, espai ampli per a la tripulació.")
    sala_sortida_exterior = Zona(9, "Sala Sortida exterior", "La sala de sortida a l'exterior. Accés directe als propulsors.")
    propulsors = Zona(10, "Propulsors", "La zona dels propulsors de la nau. Exterior amb perill d'asfíxia si no vas equipat.")

    vestuari.afegir_objecte(vestit_espacial)
    tallers.afegir_objecte(eina)
    cuina.afegir_objecte(donuts)
    oficines.afegir_objecte(targeta_identificadora)

    comandament.afegir_sortida(oficines); comandament.afegir_sortida(menjador)
    oficines.afegir_sortida(tallers); oficines.afegir_sortida(vestuari); oficines.afegir_sortida(banys); oficines.afegir_sortida(comandament)
    tallers.afegir_sortida(oficines); tallers.afegir_sortida(vestuari); tallers.afegir_sortida(banys)
    vestuari.afegir_sortida(tallers); vestuari.afegir_sortida(oficines); vestuari.afegir_sortida(cuina)
    cuina.afegir_sortida(vestuari); cuina.afegir_sortida(menjador); cuina.afegir_sortida(sala_sortida_exterior)
    menjador.afegir_sortida(comandament); menjador.afegir_sortida(cuina); menjador.afegir_sortida(dormitori); menjador.afegir_sortida(sala_sortida_exterior)
    dormitori.afegir_sortida(menjador); dormitori.afegir_sortida(banys)
    banys.afegir_sortida(oficines); banys.afegir_sortida(tallers); banys.afegir_sortida(dormitori)
    sala_sortida_exterior.afegir_sortida(cuina); sala_sortida_exterior.afegir_sortida(menjador); sala_sortida_exterior.afegir_sortida(propulsors)
    propulsors.afegir_sortida(sala_sortida_exterior)

    return dormitori

def main():
    while True:
        print("================================================")
        print("        JOC P000 Historia Conversacional        ")
        print("================================================")
        print()
        print("1. Jugar")
        print("2. Crédits")
        print("3. Crear personatge")
        print("4. Sortir")
        print()

        opcio = input("Selecciona una opció: ").strip()

        match opcio:
            case "1":
                zona_inicial = inicialitzar_mon()
                iniciar_partida(zona_inicial)
            case "2":
                print("\nCRÉDITOS")
                print("Juego creado por Izan i Xinhao\n")
            case "3":
                print("\nCrear Personatge (En desenvolupament...)\n")
            case "4":
                print("\n¡Adéu fins aviat!")
                break
            case _:
                print("\nOPCIÓ NO VÀLIDA\n")

if __name__ == "__main__":
    main()