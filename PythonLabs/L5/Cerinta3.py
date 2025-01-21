def inverted_index(documents):
    index = {}
    for doc_id, doc in enumerate(documents):
        words = set(doc.lower().split())  # Elimină duplicatele
        for word in words:
            if word not in index:
                index[word] = set()
            index[word].add(doc_id)
    return index

# Permite utilizatorului să introducă documente
def get_user_documents():
    documents = []
    print("Introduceți câte propoziții doriți. Tastați 'STOP' pentru a încheia introducerea:")
    while True:
        sentence = input("Introduceți o propoziție: ")
        if sentence.strip().lower() == "stop":
            break
        documents.append(sentence)
    return documents

# Exemplu de utilizare
documents = get_user_documents()
if documents:  # Asigurăm că lista nu e goală
    print("Indexul inversat generat este:")
    print(inverted_index(documents))
else:
    print("Nu ați introdus niciun document.")