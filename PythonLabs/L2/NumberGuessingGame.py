
"""import random

# Generăm un număr aleatoriu între 1 și 10
numar_corect = random.randint(1, 10)

# Cere utilizatorului să ghicească numărul
ghicire = int(input("Ghicește un număr între 1 și 10: "))

# Verificăm dacă ghicirea este corectă și afișăm mesajele corespunzătoare
if ghicire == numar_corect:
    print("Ai ghicit! Bravo!")
elif ghicire < numar_corect:
    print("Prea mic! Încearcă din nou.")
else:
    print("Prea mare! Încearcă din nou.")



import random

numar_corect = random.randint(1, 100)

# Permitem utilizatorului să aibă 10 încercări
incercari_maxime = 10
incercari = 0

# Începem jocul
print("Am ales un număr între 1 și 100. Încearcă să-l ghicești!")

while incercari < incercari_maxime:
    # Cere utilizatorului să ghicească numărul
    ghicire = int(input(f"Încercarea {incercari + 1}/{incercari_maxime}: Ghicește numărul: "))
    incercari += 1

    # Verificăm dacă ghicirea este corectă
    if ghicire == numar_corect:
        print(f"Felicitări! Ai ghicit numărul {numar_corect} pe încercarea {incercari}!")
        break
    elif ghicire < numar_corect:
        print("Too low! Încearcă din nou.")
    else:
        print("Too high! Încearcă din nou.")

# Dacă nu a ghicit după 10 încercări
if ghicire != numar_corect:
    print(f"Nu ai ghicit numărul! Numărul corect era {numar_corect}.")"""


import random
numar_corect=random.randint(1, 10)

incercari_maxime=10
incercari=0

print(f"Am ales un nr intre 1 si 10. Incearca sa-l ghicesti!")
while incercari<incercari_maxime:
    ghicire= int(input(f"Incercarea {incercari+1}/{incercari_maxime}: Ghiceste numarul: "))
    incercari+=1


    if ghicire== numar_corect:
        print(f"Felicitari! Ai ghicit numarul {numar_corect} la incercarea {incercari}!")
        break
    elif ghicire<numar_corect:
        print(f"too low ")
    else :
        print(f"too high")

if ghicire !=numar_corect:
    print(f"nu ai ghicit")

