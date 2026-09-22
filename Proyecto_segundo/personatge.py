class Jugador:
    def __init__(self, nom, zona_actual):
        self.nom = nom
        self.inventari = Inventari()
        self.zona_actual = zona_actual

    def moure(self, zona_nova):
        self.zona_actual = zona_nova
        print(f"{self.nom} s'ha mogut a {zona_nova.nom}")

    def agafar(self, objecte):
        self.zona_actual.objectes.remove(objecte)
        self.inventari.objectes.append(objecte)
        objecte.agafar()

    def deixar(self, objecte):
        self.inventari.objectes.remove(objecte)
        self.zona_actual.objectes.append(objecte)
        objecte.deixar()

    def utilitzar(self, objecte):
        print(f"{self.nom} utilitza {objecte.nom}")

    def parlar(self):
        print(f"{self.nom} vol parlar amb algú")


class InventariJugador(Inventari):
    def __init__(self, capacitat_maxima=5):
        super().__init__()
        self.capacitat_maxima = capacitat_maxima

    def afegir_objecte(self, objecte):                              

    def eliminar_objecte(self, objecte):
      
    def te_objecte(self, objecte):
        return objecte in self.objectes

    def mostrar_objectes(self):
      
