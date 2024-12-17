
my_tuple = ("mere", "pere", "portocale", "banane", "struguri")

element_cautat = input("Introduceți elementul pe care doriți să îl căutați: ")

if element_cautat in my_tuple:
    index = my_tuple.index(element_cautat)
    print(f"Elementul '{element_cautat}' a fost găsit la indexul {index}.")
else:
    print(f"Elementul '{element_cautat}' nu există în tuplu.")
