import math

def main():
    # Citirea numerelor de la tastatură
    num = int(input("Introdu un număr întreg pentru calcule: "))
    angle = float(input("Introdu un unghi în grade: "))

    # Calcularea rădăcinii pătrate
    sqrt_num = math.sqrt(num)
    print(f"Rădăcina pătrată a {num} este {sqrt_num}")

    # Calcularea factorialului
    factorial_num = math.factorial(num)
    print(f"Factorialul lui {num} este {factorial_num}")

    # Calcularea sinusului unghiului
    angle_radians = math.radians(angle)  # Conversia unghiului în radiani
    sin_angle = math.sin(angle_radians)
    print(f"Sinusul unghiului de {angle} grade este {sin_angle}")

if __name__ == "__main__":
    main()
