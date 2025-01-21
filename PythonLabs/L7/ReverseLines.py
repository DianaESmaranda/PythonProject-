def reverse_lines(input_file, output_file):
    """
    Citește conținutul unui fișier și creează un alt fișier unde fiecare rând este inversat.

    :param input_file: Calea către fișierul sursă.
    :param output_file: Calea către fișierul de ieșire.
    """
    # Deschide fișierul de intrare pentru citire
    with open(input_file, 'r', encoding='utf-8') as infile:
        # Citește toate liniile din fișier
        lines = infile.readlines()

    # Deschide fișierul de ieșire pentru scriere
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for line in lines:
            # Elimină newline-ul de la finalul liniei, inversează linia și adaugă un newline
            reversed_line = line.rstrip()[::-1]
            outfile.write(reversed_line + '\n')


# Exemplu de utilizare
input_file = "input.txt"
output_file = "output.txt"
reverse_lines(input_file, output_file)
print(f"Fișierul '{output_file}' a fost creat cu liniile inversate.")
