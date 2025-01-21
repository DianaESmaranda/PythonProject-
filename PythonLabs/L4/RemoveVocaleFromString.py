def remove_vowels(text):
    vowels = "aeiouAEIOUăâîĂÎÂ"

    result = ''.join([char for char in text if char not in vowels])

    return result


text = input("Introdu un șir de caractere: ")
result = remove_vowels(text)

print("Șirul fără vocale:", result)