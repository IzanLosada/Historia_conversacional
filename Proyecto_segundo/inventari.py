class Inventari:

    def __init__(self):
        self.objectes = []

    def afegir_objecte(self, objecte):
        self.objectes.append(objecte)

    def eliminar_objecte(self, objecte):
        self.objectes.remove(objecte)

    def te_objecte(self, objecte):
        return objecte in self.objectes