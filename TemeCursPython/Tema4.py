'''import string

def verifica_parola(parola):
    if len(parola) < 8:
        return False

    if not any(c.isupper() for c in parola):
        return False

    if not any(c.islower() for c in parola):
        return False

    if not any(c.isdigit() for c in parola):
        return False

    caractere_speciale = "!@#$%^&*()-_+=<>?"
    if not any(c in caractere_speciale for c in parola):
        return False

    if ' ' in parola:
        return False

    return True

parola = input("Introduceți parola: ")

este_puternica = verifica_parola(parola)

if este_puternica:
    print("Parola dvs. este puternică.")
else:
    print("Parola dvs. este slabă.")'''




#cerinta bonu: parolele separate prin virgula
import string


def verifica_parola(parola):
    if len(parola) < 8:
        return False

    if not any(c.isupper() for c in parola):
        return False

    if not any(c.islower() for c in parola):
        return False

    if not any(c.isdigit() for c in parola):
        return False

    caractere_speciale = "!@#$%^&*()-_+=<>?"
    if not any(c in caractere_speciale for c in parola):
        return False

    if ' ' in parola:
        return False

    return True


parole_input = input("Introduceți parolele (separate prin virgulă): ")

parole = [parola.strip() for parola in parole_input.split(",")]

for i, parola in enumerate(parole, 1):
    este_puternica = verifica_parola(parola)

    if este_puternica:
        print(f"Parola {i}: '{parola}' este puternică.")
    else:
        print(f"Parola {i}: '{parola}' este slabă.")





