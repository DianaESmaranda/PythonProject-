def is_palindrome(text):
    text = text.replace(" ", "").lower()
    return text == text[::-1]

input_text = input("Introdu un cuvânt sau frază: ")

if is_palindrome(input_text):
    print("Este un palindrom!")
else:
    print("Nu este un palindrom.")
