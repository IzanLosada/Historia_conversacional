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
        
tallers = Zona(1, "Tallers", "Zona dels tallers de la nau.")
oficines = Zona(2, "Oficines", "Zona de les oficines de la nau.")
banys = Zona(3, "Banys", "Els banys de la nau.")
vestuari = Zona(4, "Vestuari", "El vestuari de la nau.")
comandament = Zona(5, "Comandament", "La sala de comandament de la nau.")
dormitori = Zona(6, "Dormitori", "El dormitori de la nau.")
cuina = Zona(7, "Cuina", "La cuina de la nau.")
menjador = Zona(8, "Menjador", "El menjador de la nau.")
sala_sortida_exterior = Zona(9, "Sala Sortida exterior", "La sala de sortida a l'exterior.")
propulsors = Zona(10, "Propulsors", "La zona dels propulsors de la nau.")