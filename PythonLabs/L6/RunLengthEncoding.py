def functie(text):
    if not text:  # Verificăm dacă șirul este gol
        return ""  # Dacă șirul este gol, returnăm un șir gol

    lista = []  # O listă pentru a construi rezultatul codificat
    c = 1  # Contor pentru numărul de caractere consecutive

    # Iterăm prin șir, începând de la al doilea caracter (indexul 1)
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:  # Dacă caracterul curent este același ca cel anterior
            c += 1  # Incrementăm contorul
        else:
            # Adăugăm caracterul anterior și numărul său de apariții în lista de rezultat
            lista.append(f"{text[i - 1]}{c}")
            c = 1  # Resetăm contorul pentru următorul caracter

    # După terminarea buclei, adăugăm ultimul caracter și numărul de apariții
    lista.append(f"{text[-1]}{c}")

    # Îmbinăm lista într-un șir și returnăm rezultatul
    return "".join(lista)

# Exemplu de utilizare
text = input("Introduceți textul pentru codificare: ")
output = functie(text)
print("Rezultatul codificării RLE:", output)
