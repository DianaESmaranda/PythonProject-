class Carte:
    def __init__(self, titlu, autor, isbn):
        self.titlu = titlu
        self.autor = autor
        self.isbn = isbn
        self.este_imprumutata = False

    def __str__(self):
        return f"{self.titlu} de {self.autor} (ISBN: {self.isbn}) {'[Împrumutată]' if self.este_imprumutata else '[Disponibilă]'}"

class MembruBiblioteca:
    def __init__(self, nume):
        self.nume = nume
        self.carti_imprumutate = []

    def imprumuta_carte(self, carte):
        if not carte.este_imprumutata:
            self.carti_imprumutate.append(carte)
            carte.este_imprumutata = True
            print(f"{self.nume} a împrumutat cartea '{carte.titlu}'.")
        else:
            print(f"Cartea '{carte.titlu}' este deja împrumutată.")

    def returneaza_carte(self, carte):
        if carte in self.carti_imprumutate:
            self.carti_imprumutate.remove(carte)
            carte.este_imprumutata = False
            print(f"{self.nume} a returnat cartea '{carte.titlu}'.")
        else:
            print(f"Cartea '{carte.titlu}' nu se află în lista de cărți împrumutate de {self.nume}.")

    def __str__(self):
        carti = ", ".join([carte.titlu for carte in self.carti_imprumutate]) or "nicio carte"
        return f"{self.nume} are împrumutate: {carti}."

class Biblioteca:
    def __init__(self):
        self.carti = []

    def adauga_carte(self, carte):
        self.carti.append(carte)
        print(f"Cartea '{carte.titlu}' a fost adăugată în bibliotecă.")

    def sterge_carte(self, carte):
        if carte in self.carti:
            self.carti.remove(carte)
            print(f"Cartea '{carte.titlu}' a fost ștearsă din bibliotecă.")
        else:
            print(f"Cartea '{carte.titlu}' nu există în bibliotecă.")

    def listeaza_carti_disponibile(self):
        carti_disponibile = [carte for carte in self.carti if not carte.este_imprumutata]
        if carti_disponibile:
            print("Cărți disponibile în bibliotecă:")
            for carte in carti_disponibile:
                print(f"- {carte}")
        else:
            print("Nu există cărți disponibile în bibliotecă.")


# Cod principal
biblioteca = Biblioteca()
membri = []

# Adăugarea cărților de la tastatură
nr_carti = int(input("Câte cărți dorești să adaugi? "))
for _ in range(nr_carti):
    titlu = input("Introdu titlul cărții: ")
    autor = input("Introdu autorul cărții: ")
    isbn = input("Introdu ISBN-ul cărții: ")
    biblioteca.adauga_carte(Carte(titlu, autor, isbn))

# Adăugarea membrilor de la tastatură
nr_membri = int(input("Câți membri dorești să adaugi? "))
for _ in range(nr_membri):
    nume = input("Introdu numele membrului: ")
    membri.append(MembruBiblioteca(nume))

# Meniul interactiv
while True:
    print("\nMeniu:")
    print("1. Împrumută o carte")
    print("2. Returnează o carte")
    print("3. Listează cărțile disponibile")
    print("4. Afișează detaliile membrilor")
    print("5. Ieșire")

    optiune = input("Alege o opțiune: ")

    if optiune == "1":
        # Împrumută o carte
        nume_membru = input("Introdu numele membrului care împrumută cartea: ")
        titlu_carte = input("Introdu titlul cărții: ")

        membru_gasit = next((membru for membru in membri if membru.nume == nume_membru), None)
        carte_gasita = next((carte for carte in biblioteca.carti if carte.titlu == titlu_carte), None)

        if membru_gasit and carte_gasita:
            membru_gasit.imprumuta_carte(carte_gasita)
        else:
            print("Membru sau cartea nu există.")

    elif optiune == "2":
        # Returnează o carte
        nume_membru = input("Introdu numele membrului care returnează cartea: ")
        titlu_carte = input("Introdu titlul cărții: ")

        membru_gasit = next((membru for membru in membri if membru.nume == nume_membru), None)
        carte_gasita = next((carte for carte in biblioteca.carti if carte.titlu == titlu_carte), None)

        if membru_gasit and carte_gasita:
            membru_gasit.returneaza_carte(carte_gasita)
        else:
            print("Membru sau cartea nu există.")

    elif optiune == "3":
        # Listează cărțile disponibile
        biblioteca.listeaza_carti_disponibile()

    elif optiune == "4":
        # Afișează detaliile membrilor
        for membru in membri:
            print(membru)

    elif optiune == "5":
        # Ieșire
        print("La revedere!")
        break

    else:
        print("Opțiune invalidă. Te rog să alegi din nou.")

