import pandas as pd
import matplotlib.pyplot as plt

mtcars = pd.read_csv('mtcars.csv')

# 1. Barplot potrošnje automobila s 4, 6 i 8 cilindara
plt.figure(figsize=(8, 6))
for cyl in [4, 6, 8]:
    subset = mtcars[mtcars['cyl'] == cyl]
    plt.bar(cyl, subset['mpg'].mean(), label=f'{cyl} cilindra', alpha=0.7)
plt.title('Potrošnja automobila prema broju cilindara')
plt.xlabel('Broj cilindara')
plt.ylabel('Potrošnja (mpg)')
plt.legend()

# 2. Boxplot distribucije težine automobila s 4, 6 i 8 cilindara
plt.figure(figsize=(8, 6))
plt.boxplot([mtcars[mtcars['cyl'] == cyl]['wt'] for cyl in [4, 6, 8]], labels=['4 cilindra', '6 cilindara', '8 cilindara'])
plt.title('Distribucija težine automobila prema broju cilindara')
plt.xlabel('Broj cilindara')
plt.ylabel('Težina (lbs)')

# 3. Potrošnja automobila s ručnim i automatskim mjenjačem
plt.figure(figsize=(8, 6))
for am in [0, 1]:
    subset = mtcars[mtcars['am'] == am]
    plt.bar(am, subset['mpg'].mean(), label=f'Automatski' if am == 0 else 'Ručni', alpha=0.7)
plt.title('Potrošnja automobila prema vrsti mjenjača')
plt.xlabel('Vrsta mjenjača (0 - Automatski, 1 - Ručni)')
plt.ylabel('Potrošnja (mpg)')
plt.xticks([0, 1], ['Automatski', 'Ručni'])
plt.legend()

# 4. Odnos ubrzanja i snage automobila za ručni i automatski mjenjač
plt.figure(figsize=(8, 6))
for am in [0, 1]:
    subset = mtcars[mtcars['am'] == am]
    plt.scatter(subset['hp'], subset['qsec'], label=f'Automatski' if am == 0 else 'Ručni', alpha=0.7)
plt.title('Odnos ubrzanja i snage automobila prema vrsti mjenjača')
plt.xlabel('Snaga (hp)')
plt.ylabel('Ubrzanje (s)')
plt.legend()

# Prikaz grafova
plt.tight_layout()
plt.show()