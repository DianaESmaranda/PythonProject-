def count_words_in_file(file_path):
    # Deschide fișierul
    file = open(file_path, 'r', encoding='utf-8')

    # Citește conținutul fișierului
    content = file.read()

    # Împarte textul în cuvinte după spațiu
    words = content.split()

    # Numără lungimea listei de cuvinte
    num_words = len(words)

    # Închide fișierul
    file.close()

    # Returnează numărul total de cuvinte
    return num_words


# Exemplu de utilizare
file_path = "example.txt"
num_words = count_words_in_file(file_path)
print(f"Numărul total de cuvinte din fișier este: {num_words}")

