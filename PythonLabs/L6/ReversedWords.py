def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])

# Citirea propoziției de la tastatură
sentence = input("Introduceți o propoziție: ")
print("Propoziția inversată:", reverse_words(sentence))
