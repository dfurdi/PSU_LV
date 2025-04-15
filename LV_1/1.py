def total_euro(sati, rate):
    return sati * rate

def main():
    sati = float(input("Unesite broj radnih sati: "))
    rate = float(input("Unesite satnicu u €: "))
    print("Vaša plaća iznosi:", total_euro(sati, rate), "€")

if __name__ == "__main__":
    main()
