def dobanda(credit, timp,rate):
    dobanda= (credit*timp*rate)/100
    return dobanda
rata= float(input("Introduceti valoare rata: "))
credit= float(input("Introduceti valoare credit: "))
timp= float(input(" Introduceti valoare timp:  "))
valoare_dobanda= dobanda(credit,timp,rata)
print(f"Dobanda pentru un credit de {credit:.2f}RON la o rata de {rata:.2f}% pe {timp:.2f}ani este:{valoare_dobanda:.2f} RON ")

"""def dobanda(credit, timp, rate):
    # Calculăm dobânda
    dobanda = (credit * timp * rate) / 100
    return dobanda

# Introducem datele de la utilizator
rata = float(input("Introduceți valoarea ratei (procentual): "))
credit = float(input("Introduceți valoarea creditului: "))
timp = float(input("Introduceți valoarea timpului (în ani): "))

# Calculăm dobânda apelând funcția
valoare_dobanda = dobanda(credit, timp, rata)

# Afișăm rezultatul calculat
print(f"Dobânda pentru un credit de {credit:.2f} RON la o rată de {rata:.2f}% pe {timp:.2f} ani este: {valoare_dobanda:.2f} RON")"""

