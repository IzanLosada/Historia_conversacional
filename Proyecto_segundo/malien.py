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

    def _moure_a_sortida(self):
        if self.zona_actual and self.zona_actual.sortides:
            self.zona_actual = random.choice(self.zona_actual.sortides)

    def moure_aleatoriament(self):
        self.comptador_torn += 1
        if self.comptador_torn >= 2:
            self.comptador_torn = 0
            self._moure_a_sortida()

    def parlar(self):
        print(f"{self.nom}: *Grunyit agressiu que ressona per les parets metàl·liques...*")

    def verificar_trobada(self, zona_jugador, inventari):
        """Retorna True si el jugador sobreviu, False si perd la partida."""
        if self.zona_actual != zona_jugador:
            return True

        print(f"[¡ALERTA!]: En Malien t'ha trobat a la sala {zona_jugador.nom}!")

        donut = next((o for o in inventari.objectes if "dònut" in o.nom.lower()), None)
        if donut:
            opcio = input("Tens dònuts a l'inventari. Vols llançar-los per distreure en Malien? (s/n): ").strip().lower()
            if opcio in ["s", "si", "sí"]:
                inventari.eliminar_objecte(donut)
                print("Has llançat els dònuts! En Malien s'ha distret menjant i fuig a una altra zona.")
                self._moure_a_sortida()
                return True

        print("En Malien t'ha atacat per sorpresa. Has perdut la partida...")
        return False