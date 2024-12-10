# Unos broja
n = int(input("Unesite cijeli broj: "))

# Brojanje djelioca unetog broja
brojac_djelioca_n = 0
for i in range(1, n + 1):
    if n % i == 0:
        brojac_djelioca_n += 1

# Provera za brojeve manje od n
anti_prost = True
for i in range(1, n):
    brojac_djelioca_i = 0
    for j in range(1, i + 1):
        if i % j == 0:
            brojac_djelioca_i += 1
    if brojac_djelioca_i >= brojac_djelioca_n:
        anti_prost = False
        break

# Ispis rezultata
print(anti_prost)
print(brojac_djelioca_n)
