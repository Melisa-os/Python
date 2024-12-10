# Unos broja n
#n = int(input("Unesite broj n: "))

# Unos i ispis n brojeva jedan ispod drugog
#for i in range(n):
    #broj = int(input())
#    print(broj)
# Unos broja n
n = int(input("Unesite broj n: "))

# Petlja za unos i kasniji ispis
brojevi = ""
for _ in range(n):
    broj = int(input())
    brojevi += str(broj) + "\n"

# Ispis brojeva
print(brojevi)
