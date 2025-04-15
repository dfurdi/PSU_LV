def citanje_SMS(dat_name):
    try:
        with open(dat_name, 'r') as file:
            ham_broj_rijeci = 0
            ham_broj_poruka = 0
            spam_broj_rijeci = 0
            spam_broj_poruka = 0
            spam_usklicnik = 0
            
            for linija in file:
                dijelovi = linija.strip().split('\t')
                if len(dijelovi) == 2:
                    oznaka, poruka = dijelovi
                    rijeci = poruka.split()
                    if oznaka == 'ham':
                        ham_broj_poruka += 1
                        ham_broj_rijeci += len(rijeci)
                    elif oznaka == 'spam':
                        spam_broj_poruka += 1
                        spam_broj_rijeci += len(rijeci)
                        if poruka.endswith('!'):
                            spam_usklicnik += 1
            
            if ham_broj_poruka > 0:
                prosjecan_broj_rijeci_ham = ham_broj_rijeci / ham_broj_poruka
                print(f"Prosjecan broj rijeci u ham porukama: {prosjecan_broj_rijeci_ham}")
            else:
                print("Nema ham poruka.")
                
            if spam_broj_poruka > 0:
                prosjecan_broj_rijeci_spam = spam_broj_rijeci / spam_broj_poruka
                print(f"Prosjecan broj rijeci u spam porukama: {prosjecan_broj_rijeci_spam}")
                print(f"Broj spam poruka koje zavrsavaju usklicnikom: {spam_usklicnik}")
            else:
                print("Nema spam poruka.")
    except FileNotFoundError:
        print("Datoteka nije pronađena.")

ime_datoteke = "SMSSpamCollection.txt"
citanje_SMS(ime_datoteke)