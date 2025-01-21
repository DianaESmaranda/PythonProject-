celsius_temp= float(input("Introduceti temperatura in grade celsius: "))
def celsius_to_fahrenheit(celsius_temp):
    fahrenheit= (9/5)*celsius_temp +32
    return fahrenheit
fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp}C este egal cu {fahrenheit_temp}°F")
