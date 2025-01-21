def filter_lines(input_file, output_file, keyword):
    """
    Citește conținutul unui fișier și creează un alt fișier care conține doar liniile ce includ un cuvânt cheie specific.

    :param input_file: Calea către fișierul sursă.
    :param output_file: Calea către fișierul de ieșire.
    :param keyword: Cuvântul cheie pe care îl căutăm în linii.
    """
    # Deschide fișierul de intrare pentru citire
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    # Deschide fișierul de ieșire pentru scriere
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for line in lines:
            # Verifică dacă cuvântul cheie este în linie
            if keyword.lower() in line.lower():  # Ignoră diferențele de majuscule/micuscule
                outfile.write(line)


# Exemplu de utilizare
input_file = "input.txt"
output_file = "filtered.txt"
keyword = "Python"
filter_lines(input_file, output_file, keyword)
print(f"Fișierul '{output_file}' a fost creat cu liniile care conțin cuvântul '{keyword}'.")
