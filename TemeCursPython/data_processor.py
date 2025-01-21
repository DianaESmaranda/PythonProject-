import csv

def read_csv(file_path):
    """
    Citește un fișier CSV și returnează conținutul ca o listă de dicționare.
    :param file_path: Calea către fișierul CSV
    :return: Listă de dicționare cu conținutul fișierului
    """
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]

def filter_data(data, key, value):
    """
    Filtrează o listă de dicționare pe baza unei perechi cheie-valoare.
    :param data: Listă de dicționare
    :param key: Cheia după care se face filtrarea
    :param value: Valoarea care trebuie să corespundă pentru filtrare
    :return: Listă filtrată de dicționare
    """
    return [row for row in data if row.get(key) == value]

def write_csv(data, file_path):
    """
    Scrie o listă de dicționare într-un fișier CSV.
    :param data: Listă de dicționare
    :param file_path: Calea către fișierul CSV în care se scriu datele
    """
    if not data:
        raise ValueError("Datele furnizate sunt goale și nu pot fi scrise într-un fișier CSV.")

    with open(file_path, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
