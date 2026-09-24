class Zona:
    def __init__(self, id, nom, descripcio):
        self.id = id
        self.nom = nom
        self.descripcio = descripcio
        self.sortides = []
        self.personatges = []
        self.objectes = []

    def mostrar_descripcio(self):
        print(self.descripcio)

    def afegir_objecte(self, objecte):
        self.objectes.append(objecte)

    def afegir_sortida(self, zona):
        self.sortides.append(zona)

    def eliminar_objecte(self, objecte):
        self.objectes.remove(objecte)