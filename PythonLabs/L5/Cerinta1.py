import string


def word_frequency(text):
    # Eliminăm semnele de punctuație și convertim textul la litere mici
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator).lower()

    # Separăm cuvintele
    words = text.split()

    # Calculăm frecvența fiecărui cuvânt
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency