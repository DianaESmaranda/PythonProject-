import re

def count_word_occurrences(sentence, word):

    sentence = sentence.lower()
    word = word.lower()

    sentence = re.sub(r'[^\w\s]', '', sentence)

    words = sentence.split()

    return words.count(word)

sentence = input("Introduceți propoziția: ")
word = input("Introduceți cuvântul pe care doriți să-l numărați: ")

occurrences = count_word_occurrences(sentence, word)
print(f"Cuvântul '{word}' apare de {occurrences} ori în propoziție.")
