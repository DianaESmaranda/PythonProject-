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

# Exemplu de utilizare
biblioteca = Biblioteca()

# Adăugarea cărților
carti = [
    Carte("1984", "George Orwell", "1234567890"),
    Carte("Mândrie și prejudecată", "Jane Austen", "0987654321"),
    Carte("Crimă și pedeapsă", "Fyodor Dostoevsky", "1122334455"),
    Carte("Odiseea", "Homer", "6677889900"),
    Carte("Frankenstein", "Mary Shelley", "5566778899")
]
for carte in carti:
    biblioteca.adauga_carte(carte)

# Crearea membrilor bibliotecii
membri = [
    MembruBiblioteca("Ana"),
    MembruBiblioteca("Ion"),
    MembruBiblioteca("Maria")
]

# Simularea împrumutării și returnării cărților
membri[0].imprumuta_carte(carti[0])  # Ana împrumută "1984"
membri[1].imprumuta_carte(carti[0])  # Ion încearcă să împrumute "1984", dar este deja împrumutată
membri[1].imprumuta_carte(carti[1])  # Ion împrumută "Mândrie și prejudecată"
membri[2].imprumuta_carte(carti[2])  # Maria împrumută "Crimă și pedeapsă"

# Listarea cărților disponibile
biblioteca.listeaza_carti_disponibile()

# Returnarea cărților
membri[0].returneaza_carte(carti[0])  # Ana returnează "1984"
membri[1].imprumuta_carte(carti[0])  # Ion împrumută "1984"

# Listarea cărților disponibile după returnare
biblioteca.listeaza_carti_disponibile()

# Afișarea detaliilor despre membri
for membru in membri:
    print(membru)
