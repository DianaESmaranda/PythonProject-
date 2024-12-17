def calculeaza_factorial():
    try:
        n = int(input("Introdu un număr întreg pozitiv pentru a calcula factorialul: "))

        if n < 0:
            print("Factorialul nu este definit pentru numere negative.")
            return
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i


        print(f"Factorialul lui {n} este {factorial}.")

    except ValueError:
        print("Te rog să introduci un număr întreg valid.")

calculeaza_factorial()


