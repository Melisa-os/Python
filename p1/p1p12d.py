# Unos dužine stranice kvadrata n
n = int(input("Unesite dužinu stranice kvadrata: "))

# Početna dužina zmije
duzina_zmije = 1

# Broj hrane koju zmija može pojesti
broj_hrane = 0

# Dok zmija može da raste
while duzina_zmije <= n * n:
    # Povećaj broj hrane koju zmija može pojesti
    broj_hrane += 1
    # Udvostruči dužinu zmije
    duzina_zmije *= 2

# Ispis rezultata
print(broj_hrane - 1)  # Oduzima se 1 jer poslednje udvostručenje prelazi granicu
