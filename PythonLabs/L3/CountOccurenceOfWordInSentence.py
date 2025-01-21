from collections import Counter


def count_word_occurrences(sentence):
    words = sentence.split()# Împărțim propoziția în cuvinte și folosim Counter pentru a număra aparițiile
    word_count = Counter(words)


    for word, count in word_count.items():
        print(f"Cuvântul '{word}' apare de {count} ori.")


sentence = input("Introduceti o propoziție pentru a număra cuvintele: ")

count_word_occurrences(sentence)# Apelăm funcția pentru a număra cuvintele