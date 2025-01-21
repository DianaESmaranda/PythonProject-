import math


def calculate_distance(x1, y1, x2, y2):

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance


# Introducerea coordonatelor de la tastatură
x1 = float(input("Introduceți coordonata x1: "))
y1 = float(input("Introduceți coordonata y1: "))
x2 = float(input("Introduceți coordonata x2: "))
y2 = float(input("Introduceți coordonata y2: "))


distance = calculate_distance(x1, y1, x2, y2)
print(f"Distanța dintre punctele ({x1}, {y1}) și ({x2}, {y2}) este {distance:.2f}")
