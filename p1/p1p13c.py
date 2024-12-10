# Unos prirodnog broja n
n = input("Unesite prirodan broj sa parnim brojem cifara: ")

# Provera parova cifara
ispravnost = True
duzina = len(n)
for i in range(0, duzina, 2):
    x = int(n[i])
    y = int(n[i + 1])
    if n.count(str(y)) != x:
        ispravnost = False
        break

# Ispis rezultata
if ispravnost:
    print("True")
else:
    print("False")
