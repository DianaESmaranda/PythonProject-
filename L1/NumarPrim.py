numar=int(input("Introduceti un nr intreg: "))
if numar<=1:
    print(f"numar NU e prim")
else:
    for i in range (2, int(numar**0.5+1)):
        if numar%i==0:
            print(f"NU e prim")
            break

    else:
            print(f"Numarul {numar} este prim")

