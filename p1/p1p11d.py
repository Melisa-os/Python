# Unos cene artikla, troška postavljanja, procenata i troška izrade
c = float(input("Unesite cenu artikla (u KM): "))
t = float(input("Unesite trošak postavljanja artikla na prodaju (u KM): "))
p = float(input("Unesite procenat koji ide stranici prodaja.ba: "))
i = float(input("Unesite trošak izrade artikla (u KM): "))

# Računanje preostalog iznosa nakon troška postavljanja artikla
preostalo_posle_troska_postavljanja = c - t

# Računanje iznosa koji ide stranici prodaja.ba
deo_za_prodaja_ba = preostalo_posle_troska_postavljanja * p

# Računanje preostalog iznosa za korisnika posle oduzimanja dela za prodaja.ba
preostalo_za_korisnika = preostalo_posle_troska_postavljanja - deo_za_prodaja_ba

# Računanje konačnog profita korisnika posle oduzimanja troška izrade
konacni_profit = preostalo_za_korisnika - i

# Ispis rezultata zaokružen na dve decimale
print(round(konacni_profit, 2))
