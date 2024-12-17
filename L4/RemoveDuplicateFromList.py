
def remove_duplicates(lst):
    lista_fara_duplicate = []
    vazut = set()

    for element in lst:
        if element not in vazut:
            lista_fara_duplicate.append(element)
            vazut.add(element)

    return lista_fara_duplicate


valori = input("Introduceți valorile separate prin spațiu: ")


lista = valori.split()

lista = [int(x) for x in lista] 

lista_fara_duplicate = remove_duplicates(lista)

print("Lista fără duplicate:", lista_fara_duplicate)
