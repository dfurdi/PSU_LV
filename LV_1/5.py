def brojac_funkc(imedat):
    try:
        brojac = {}
        with open(imedat, 'r') as file:
            for linija in file:
                rijeci = linija.strip().split()
                for rijec in rijeci:
                    brojac[rijec] = brojac.get(rijec, 0) + 1
        
        broj_jedin_rijeci = sum(1 for broj in brojac.values() if broj == 1)

        print("Broj riječi koje se pojavljuju samo jednom:", broj_jedin_rijeci)
        print("Jedinstvene riječi:")
        
        for rijec, broj in brojac.items():
            if broj == 1:
                print(rijec)
    except FileNotFoundError:
        print("Datoteka nije pronađena.")


imedat = input("Ime datoteke: ")
brojac_funkc(imedat)
