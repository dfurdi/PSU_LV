lista = []
while True:
    try:
        unos = input("Unesite broj ili 'done' za izlazak iz petlje: ")
        if unos.lower() == 'done':
            break
        broj = float(unos)
        lista.append(broj)
    except ValueError:
        print("Unijeli ste pogresnu vrijednost. Unesite broj ili done za izlazak iz petlje.")

if len(lista) == 0:
    print("Lista je prazna.")
else:
    print("Brojeva uneseno: ", len(lista))
    print("Srednja vrijednost: ", sum(lista) / len(lista))
    print("Minimalna vrijednost: ", min(lista))
    print("Maksimalna vrijednost: ", max(lista))

    lista.sort()
    print("Sortirana lista brojeva", lista)
    
