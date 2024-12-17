
numere = input("Introduceți numerele separate prin spațiu: ")


lista_numere = list(map(float, numere.split()))

valoare_max = max(lista_numere)
valoare_min = min(lista_numere)

print(f"Valoarea maximă: {valoare_max}")
print(f"Valoarea minimă: {valoare_min}")
