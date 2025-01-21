# main.py

import MathOperations

def main():
    # Introducerea a două numere de la tastatură
    num1 = float(input("Introdu primul număr: "))
    num2 = float(input("Introdu al doilea număr: "))

    # Efectuarea operațiilor matematice utilizând funcțiile din MathOperations.py
    suma = MathOperations.adunare(num1, num2)
    print(f"Suma este: {suma}")

    diferenta = MathOperations.scadere(num1, num2)
    print(f"Diferența este: {diferenta}")

    produsul = MathOperations.inmultire(num1, num2)
    print(f"Produsul este: {produsul}")

    try:
        impartirea = MathOperations.impartire(num1, num2)
        print(f"Împărțirea este: {impartirea}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
