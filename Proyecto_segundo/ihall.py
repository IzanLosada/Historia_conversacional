import random

class IHall:
    def __init__(self, nom="iHall"):
        self.nom = nom

    def interaccio_torn(self, joc_context):
        vol_parlar = input(f"\nVols parlar amb l'ordinador {self.nom} en aquest torn? (s/n): ").strip().lower()
        if vol_parlar not in ["s", "si", "sí"]:
            print(f"\n[{self.nom}]: Silenci de ràdio mantingut.")
            return

        print(f"\n[{self.nom}]: Digues, capità Bond. Què necessites saber?")
        print("1. On està la llanterna?")
        print("2. On està el Malien?")
        
        opcio = input("Tria una opció (1 o 2): ").strip()

        if opcio == "1":
            ubicacio_real = joc_context.get("ubicacio_llanterna")
            llista_h = joc_context.get("totes_habitacions")
            print(self.preguntar_llanterna(ubicacio_real, llista_h))
        elif opcio == "2":
            ubicacio_m = joc_context.get("ubicacio_malien")
            print(self.preguntar_malien(ubicacio_m))
        else:
            print(f"\n[{self.nom}]: Opció no vàlida. Continuem amb la missió.")

    def preguntar_llanterna(self, ubicacio_real, llista_habitacions):
        encerta = random.choice([True, False])
        if encerta:
            return f"\n[{self.nom}]: He revisat els mapes tèrmics. La llanterna està situada exactament a: **{ubicacio_real}**."
        else:
            habitacions_falsas = [h for h in llista_habitacions if h != ubicacio_real]
            mentira = random.choice(habitacions_falsas) if habitacions_falsas else "a l'espai exterior"
            return f"\n[{self.nom}]: Segons els meus càlculs... crec que vas deixar la llanterna a **{mentira}**... o potser no. Recorda que la meva memòria de vegades falla!"

    def preguntar_malien(self, ubicacio_malien):
        return f"\n[{self.nom}]: Alerta màxima! Els sensors de moviment detecten la presència del 'Malien' a la zona de: **{ubicacio_malien}**."