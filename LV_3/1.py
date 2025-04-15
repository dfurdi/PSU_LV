import pandas as pd

mtcars = pd.read_csv('mtcars.csv')

mtcars['Weight_kg'] = mtcars['wt'] * 0.453592

#Pitanje 1:
velikapotrosnja = mtcars.sort_values(by='mpg', ascending=False).head(5)
#Pitanje 2:
malapotrosnja_8 = mtcars[mtcars['cyl'] == 8].sort_values(by='mpg').head(3)
#Pitanje 3:
prosjekpotr_6 = mtcars[mtcars['cyl'] == 6]['mpg'].mean()
#Pitanje 4:
prosjekpotr_4_lbs = mtcars[(mtcars['cyl'] == 4) & (mtcars['wt'] >= 2.0) & (mtcars['wt'] <= 2.2)]['mpg'].mean()
#Pitanje 5:
manual = mtcars[mtcars['am'] == 0]['am'].count()
automatik = mtcars[mtcars['am'] == 1]['am'].count()
#Pitanje 6:
automatik_100ks = mtcars[(mtcars['am'] == 0) & (mtcars['hp'] > 100)]['am'].count()
#Pitanje 7:
masa = mtcars[['car', 'Weight_kg']]

#Ispis i poziv funkcija
print("1. Kojih 5 automobila ima najvecu potrosnju? ")
print(velikapotrosnja[['car', 'mpg']])
print("\n2. Koja tri automobila s 8 cilindara imaju najmanju potrosnju?")
print(malapotrosnja_8[['car', 'mpg']])
print("\n3. Kolika je srednjan potrošnja automobila sa 6 cilindara?")
print(prosjekpotr_6)
print("\n4. Kolika je srednja potrosnja automobila sa 4 cilindra mase izmedju 2000 i 2200 lbs?")
print(prosjekpotr_4_lbs)
print("\n5. Koliko je automobila s rucnim, a koliko s automatskim mjenjacem?")
print("Rucni mjenjac: ", manual)
print("Automatski mjenjac:", automatik)
print("\nKoliko je automobila s automatskim mjenjacem i snagom preko 100 konjskih snaga?")
print(automatik_100ks)
print("\n7. Masa svakog automobila u kg: ")
print(masa)