# Unos dva broja n i m
n = int(input("Unesite prvi broj n: "))
m = int(input("Unesite drugi broj m: "))

# Pronalazak prve naredne vrednosti veće od oba broja, koja je deljiva sa m
broj = max(n, m) + 1
while broj % m != 0:
    broj += 1

# Ispis rezultata
print(broj)
