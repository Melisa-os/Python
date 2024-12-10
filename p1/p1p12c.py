# Unos dana, meseca, godine i broja n
dan = int(input("Unesite dan: "))
mesec = int(input("Unesite mesec: "))
godina = int(input("Unesite godinu: "))
n = int(input("Unesite broj dana: "))

# Broj dana u svakom mesecu (neprijestupna godina)
dani_u_mesecu = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

# Dodavanje dana
dan += n

# Ažuriranje datuma
while True:
    if dan > dani_u_mesecu[mesec]:
        dan -= dani_u_mesecu[mesec]
        mesec += 1
        if mesec > 12:
            mesec = 1
            godina += 1
    else:
        break

# Ispis rezultata u traženom formatu
print(f"{dan}. {mesec}. {godina}")
