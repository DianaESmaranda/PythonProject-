# math_operations.py

def adunare(a, b):
    """Returnează suma a două numere."""
    return a + b

def scadere(a, b):
    """Returnează diferența dintre două numere."""
    return a - b

def inmultire(a, b):
    """Returnează produsul a două numere."""
    return a * b

def impartire(a, b):
    """Returnează împărțirea a două numere.
    Aruncă o eroare dacă se încearcă împărțirea la zero."""
    if b == 0:
        raise ValueError("Împărțirea la zero nu este permisă!")
    return a / b
