from inventari import Inventari

import random
class Jugador:
    def __init__(self, nom, zona_actual):
        self.nom = nom
        self.inventari = Inventari()
        self.zona_actual = zona_actual

    def moure(self, nova_zona):
        if nova_zona in self.zona_actual.sortides:
            self.zona_actual = nova_zona
            print(f"T'has mogut a {nova_zona.nom}")
            nova_zona.mostrar_descripcio()
        else:
            print("No pots anar cap allà des d'aquí.")

    def agafar(self, objecte):
        if objecte in self.zona_actual.objectes:
            self.zona_actual.eliminar_objecte(objecte)
            self.inventari.afegir_objecte(objecte)
            objecte.agafar()
        else:
            print(f"Aquí no hi ha cap {objecte.nom}.")

    def deixar(self, objecte):
        if self.inventari.te_objecte(objecte):
            self.inventari.eliminar_objecte(objecte)
            self.zona_actual.afegir_objecte(objecte)
            objecte.deixar()
        else:
            print(f"No portes {objecte.nom} a l'inventari.")

    def utilitzar(self, objecte):
        if self.inventari.te_objecte(objecte):
            objecte.utilitzar()
        else:
            print(f"No pots utilitzar {objecte.nom} perquè no el tens.")

    def parlar(self, personatge):
        if personatge in self.zona_actual.personatges:
            personatge.parlar()
        else:
            print("Aquí no hi ha ningú amb qui parlar.")

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
