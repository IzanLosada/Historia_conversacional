class Objecte:
    def __init__(self, id, nom, descripcio):
        self.id = id
        self.nom = nom
        self.descripcio = descripcio

    def agafar(self):
        print(f"Has agafat {self.nom}")

    def deixar(self):
        print("Has deixat ", self.nom)
        
#Creem els objectes
llanterna = Objecte(1, "Llanterna", "Una llanterna que permet il·luminar la nau.")
eina = Objecte(2, "Eina", "Una eina especial per reparar els propulsors.")
vestit_espacial = Objecte(3, "Vestit espacial", "Un vestit d'astronauta.")
targeta_id = Objecte(4, "Targeta identificadora", "La targeta personal del capità Bond.")
targeta_company = Objecte(5, "Targeta identificadora company", "La targeta d'un company.")
donuts = Objecte(6, "Dònuts", "Uns dònuts per distreure en Malien.")

class Inventari:
    def __init__(self):
        self.objectes = []

    def afegir_objecte(self, objecte):
        self.objectes.append(objecte)

    def eliminar_objecte(self, objecte):
        pass

    def te_objecte(self, objecte):
        pass

    def mostrar_objectes(self):
        pass
    
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

class Jugador:
    def __init__(self, nom, zona_actual):
        self.nom = nom
        self.inventari = Inventari()
        self.zona_actual = zona_actual

    def moure(self):
        pass

    def agafar(self, objecte):
        pass

    def deixar(self, objecte):
        pass

    def utilitzar(self, objecte):
        pass

    def parlar(self):
        pass
    
class Personatge:
    def __init__(self, nom, descripcio, zona_actual):
        self.nom = nom
        self.descripcio = descripcio
        self.zona_actual = zona_actual

    def parlar(self):
        pass

    def moure(self):
        pass
    
class PersonatgeNPC(Personatge):
    def __init__(self, nom, descripcio, zona_actual, frases):
        super().__init__(nom, descripcio, zona_actual)
        self.frases = frases

    def reaccionar(self):
        pass

    def donar_objecte(self):
        pass

    def bloquejar_sortida(self):
        pass
    
class Malien(PersonatgeNPC):
    def moure(self):
        pass

    def atacar(self):
        pass

    def interactuar(self, objecte):
        pass