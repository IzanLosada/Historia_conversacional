import random
from personatge import Personatge

class Malien(Personatge):
    def __init__(self, zona_inicial):
        super().__init__(
            nom="Malien",
            descripcio="Una criatura alienígena hostil que ronda per la nau.",
            zona_actual=zona_inicial
        )
        self.comptador_torn = 0

    def moure_aleatoriament(self):
        self.comptador_torn += 1
        if self.comptador_torn >= 2:
            self.comptador_torn = 0
            if self.zona_actual and self.zona_actual.sortides:
                self.zona_actual = random.choice(self.zona_actual.sortides)

    def parlar(self):
        print(f"\n{self.nom}: *Grunyit agressiu que ressona per les parets metàl·liques...*")

    def verificar_trobada(self, jugador):
        if self.zona_actual == jugador.zona_actual:
            print(f"\n[¡ALERTA!]: En Malien t'ha trobat a la sala {jugador.zona_actual.nom}!")
            
            te_donuts = False
            donut_obj = None
            for obj in jugador.inventari.objectes:
                if "dònut" in obj.nom.lower() or "donuts" in obj.nom.lower():
                    te_donuts = True
                    donut_obj = obj
                    break

            if te_donuts:
                opcio = input("Tens dònuts a l'inventari. Vols llançar-los per distreure en Malien? (s/n): ").strip().lower()
                if opcio in ["s", "si", "sí"]:
                    jugador.inventari.eliminar_objecte(donut_obj)
                    print("\nHas llançat els dònuts! En Malien s'ha distret menjant i fuig a una altra zona.")
                    if self.zona_actual.sortides:
                        self.zona_actual = random.choice(self.zona_actual.sortides)
                    return True
            
            print("\nEn Malien t'ha atacat per sorpresa. Has perdut la partida...")
            return False
        return True