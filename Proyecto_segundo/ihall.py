import random

class IHall:
    def __init__(self, nom="iHall"):
        self.nom = nom

    def interaccio_torn(self, joc_context):
        vol_parlar = input(f"\nVols parlar amb l'ordinador {self.nom} en aquest torn? (s/n): ").strip().lower()
        if vol_parlar not in ["s", "si", "sí"]:
            print(f"[{self.nom}]: Silenci de ràdio mantingut.")
            return

        print(f"[{self.nom}]: Digues, capità Bond. Què necessites saber?")
        print("1. On està la llanterna?")
        print("2. On està el Malien?")

        opcio = input("Tria una opció (1 o 2): ").strip()

        if opcio == "1":
            print(self.preguntar_llanterna(joc_context["ubicacio_llanterna"], joc_context["totes_habitacions"]))
        elif opcio == "2":
            print(self.preguntar_malien(joc_context["ubicacio_malien"]))
        else:
            print(f"[{self.nom}]: Opció no vàlida. Continuem amb la missió.")

    def preguntar_llanterna(self, ubicacio_real, llista_habitacions):
        if random.choice([True, False]):
            return f"[{self.nom}]: He revisat els mapes tèrmics. La llanterna està situada exactament a: **{ubicacio_real}**."

        falses = [h for h in llista_habitacions if h != ubicacio_real]
        mentira = random.choice(falses) if falses else "a l'espai exterior"
        return f"[{self.nom}]: Segons els meus càlculs... crec que vas deixar la llanterna a **{mentira}**... o potser no. Recorda que la meva memòria de vegades falla!"

    def preguntar_malien(self, ubicacio_malien):
        return f"[{self.nom}]: Alerta màxima! Els sensors de moviment detecten la presència del 'Malien' a la zona de: **{ubicacio_malien}**."