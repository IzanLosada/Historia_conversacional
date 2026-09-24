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
