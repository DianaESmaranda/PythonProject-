numar= int(input("Introdu un nr intreg: "))
def f_grade(numar):
    if numar>=90:
        return "A"
    elif numar>=80:
        return "B"
    elif numar>=70:
        return "C"
    elif numar>=60:
        return "D"
    elif numar<60:
        return "F"
litera= f_grade(numar)
print(f"Nota corespunzatoare este: {litera}")