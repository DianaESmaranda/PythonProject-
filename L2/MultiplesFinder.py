def find_multiples(number, start, end):
    if number == 0:
        return "Numărul trebuie să fie diferit de zero!"
    multiples = [i for i in range(start, end + 1) if i % number == 0]
    return multiples

numar = int(input("Introdu un număr: "))
inceput = int(input("Introdu începutul intervalului: "))
sfarsit = int(input("Introdu sfârșitul intervalului: "))

multipli = find_multiples(numar, inceput, sfarsit)
print(f"Multiplii lui {numar} între {inceput} și {sfarsit} sunt: {multipli}")
