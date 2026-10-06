import random

class Personatge:
    def __init__(self, nom, descripcio, zona_actual):
        self.nom = nom
        self.descripcio = descripcio
        self.zona_actual = zona_actual

    def parlar(self):
        print(f"{self.nom}: ...")

    def moure(self, nova_zona):
        self.zona_actual = nova_zona

class PersonatgeNPC(Personatge):
    def __init__(self, nom, descripcio, zona_actual, frases):
        super().__init__(nom, descripcio, zona_actual)
        self.frases = frases
        self.objecte = None
        self.sortida_bloquejada = None

    def parlar(self):
        self.reaccionar()

    def reaccionar(self):
        print(f"{self.nom}: {random.choice(self.frases)}")

    def donar_objecte(self, jugador):
        if self.objecte:
            jugador.inventari.afegir_objecte(self.objecte)
            print(f"{self.nom} et dona: {self.objecte.nom}")
            self.objecte = None
        else:
            print(f"{self.nom} no té res per donar-te.")

    def bloquejar_sortida(self, zona):
        self.sortida_bloquejada = zona