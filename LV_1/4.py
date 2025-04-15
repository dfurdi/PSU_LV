def average(dat_name):
    try:
        with open(dat_name, 'r') as file:
            ukupno = 0
            br_linija = 0
            for linija in file:
                if linija.startswith("X-DSPAM-Confidence:"):
                    try:
                        ukupno += float(linija.split(":")[1].strip())
                        br_linija += 1
                    except ValueError:
                        continue
            if br_linija > 0:
                sred_pouzdanost = ukupno / br_linija
                print(f"Average X DSPAM-Confidence: {sred_pouzdanost}")
            else:
                print("Nema linija s pouzdanoscu.")
    except FileNotFoundError:
        print("Datoteka nije pronadjena.")

dat_name = input("Ime datoteke: ")
average(dat_name)        