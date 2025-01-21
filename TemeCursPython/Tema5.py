import os

def citeste_filme(fisier):
    """Citeste filmele din fisier si le returneaza ca un dictionar."""
    filme = {}
    if os.path.exists(fisier):
        with open(fisier, 'r') as f:
            for linie in f:
                linie = linie.strip()
                if linie:
                    titlu, evaluare = linie.rsplit(',', 1)
                    filme[titlu.strip()] = int(evaluare.strip())
    return filme

def scrie_filme(fisier, filme):
    """Scrie filmele si evaluarile in fisier."""
    with open(fisier, 'w') as f:
        for titlu, evaluare in sorted(filme.items(), key=lambda x: x[1], reverse=True):
            f.write(f"{titlu}, {evaluare}\n")

def afiseaza_filme(filme):
    """Afiseaza lista de filme sortata dupa evaluare."""
    if not filme:
        print("Nu exista filme in lista.")
    else:
        print("\nLista de filme:")
        for titlu, evaluare in sorted(filme.items(), key=lambda x: x[1], reverse=True):
            print(f"{titlu}: {evaluare}")

def adauga_film(filme):
    """Permite utilizatorului sa adauge un film nou."""
    titlu = input("Introdu titlul filmului: ").strip()
    if titlu in filme:
        print("Filmul exista deja in lista. Foloseste optiunea de actualizare pentru a schimba evaluarea.")
        return
    evaluare = valideaza_evaluare()
    filme[titlu] = evaluare
    print(f"Filmul '{titlu}' a fost adaugat cu evaluarea {evaluare}.")

def actualizeaza_film(filme):
    """Permite utilizatorului sa actualizeze evaluarea unui film existent."""
    titlu = input("Introdu titlul filmului pe care vrei sa-l actualizezi: ").strip()
    if titlu not in filme:
        print("Filmul nu exista in lista.")
        return
    evaluare = valideaza_evaluare()
    filme[titlu] = evaluare
    print(f"Evaluarea filmului '{titlu}' a fost actualizata la {evaluare}.")

def sterge_film(filme):
    """Permite utilizatorului sa stearga un film din lista."""
    titlu = input("Introdu titlul filmului pe care vrei sa-l stergi: ").strip()
    if titlu in filme:
        del filme[titlu]
        print(f"Filmul '{titlu}' a fost sters din lista.")
    else:
        print("Filmul nu exista in lista.")

def valideaza_evaluare():
    """Valideaza evaluarea introdusa de utilizator."""
    while True:
        try:
            evaluare = int(input("Introdu o evaluare (1-5): ").strip())
            if 1 <= evaluare <= 5:
                return evaluare
            else:
                print("Evaluarea trebuie sa fie intre 1 si 5. Mai incearca.")
        except ValueError:
            print("Te rog introdu un numar valid.")

def meniu():
    """Afiseaza meniul si returneaza optiunea aleasa de utilizator."""
    print("\nSistem de Evaluare a Filmelor")
    print("1. Vizualizeaza toate filmele")
    print("2. Adauga un film nou")
    print("3. Actualizeaza evaluarea unui film")
    print("4. Sterge un film")
    print("5. Salveaza si iesi")
    return input("Alege o optiune (1-5): ").strip()

def main():
    fisier = "movies.txt"
    filme = citeste_filme(fisier)

    while True:
        optiune = meniu()
        if optiune == '1':
            afiseaza_filme(filme)
        elif optiune == '2':
            adauga_film(filme)
        elif optiune == '3':
            actualizeaza_film(filme)
        elif optiune == '4':
            sterge_film(filme)
        elif optiune == '5':
            scrie_filme(fisier, filme)
            print("Modificarile au fost salvate. La revedere!")
            break
        else:
            print("Optiune invalida. Te rog alege o optiune intre 1 si 5.")

if __name__ == "__main__":
    main()
