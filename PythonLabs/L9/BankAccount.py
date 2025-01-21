class BankAccount:
    def __init__(self):
        """
        Initializează un cont bancar cu un sold inițial de 0.
        """
        self._balance = 0  # Atribut privat pentru a proteja soldul

    def deposit(self, amount):
        """
        Adaugă o sumă specificată în cont.

        :param amount: Suma de adăugat (trebuie să fie un număr pozitiv).
        """
        if amount > 0:
            self._balance += amount
            print(f"Depunere reușită: {amount} unități. Sold curent: {self._balance} unități.")
        else:
            print("Suma trebuie să fie mai mare decât 0.")

    def withdraw(self, amount):
        """
        Retrage o sumă specificată din cont, dacă există suficient sold.

        :param amount: Suma de retras (trebuie să fie un număr pozitiv).
        """
        if amount > 0:
            if amount <= self._balance:
                self._balance -= amount
                print(f"Retragere reușită: {amount} unități. Sold curent: {self._balance} unități.")
            else:
                print("Fonduri insuficiente.")
        else:
            print("Suma trebuie să fie mai mare decât 0.")

    def get_balance(self):
        """
        Returnează soldul curent al contului.

        :return: Soldul curent al contului.
        """
        return self._balance

# Exemplu de utilizare cu introducere de la tastatură
cont = BankAccount()

while True:
    print("\n1. Depunere\n2. Retragere\n3. Afișare sold\n4. Ieșire")
    optiune = input("Alegeți o opțiune: ")

    if optiune == "1":
        try:
            suma = float(input("Introduceți suma de depus: "))
            cont.deposit(suma)
        except ValueError:
            print("Introduceți o valoare numerică validă.")

    elif optiune == "2":
        try:
            suma = float(input("Introduceți suma de retras: "))
            cont.withdraw(suma)
        except ValueError:
            print("Introduceți o valoare numerică validă.")

    elif optiune == "3":
        print(f"Soldul curent este: {cont.get_balance()} unități.")

    elif optiune == "4":
        print("Ieșire din aplicație. La revedere!")
        break

    else:
        print("Opțiune invalidă. Vă rugăm să încercați din nou.")
