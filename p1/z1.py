#napisati program u pythonu koji od korisnika trazi unos cijelog broja n.Ukoliko je uneseni broj manji ili jednak
# o,program ispisuje adekvatnu poruku.U suprotnom program ispisuje vrijednost
# (n**d(n) + sin**2(n))/(sqrt(cos**2n+4 *(3n))) zaokruzenu na 3 decimale pri cemu je d(n) zadnja cifra broja n
import math
n=int(input("Unesite cijeli broj: "))
if n <= 0:
    print("Uneseni broj mora biti veci od 0.")
else:
    d_n = n % 10
    rezultat = (n ** d_n + math.sin(n) ** 2) / (math.sqrt(math.cos(n) ** 2+4*(3*n)))
    print(f"Rezultat: {round(rezultat, 3)}")
   # izraz = (n ** d + sin(n) ** 2) / sqrt(cos(3 * n) ** (2 * n + 4))

#d_n= n % 10
#rezultat = (n ** d_n + math.sin(n) ** 2) / (math.sqrt(math.cos(n) ** 2 + 4 * (3 * n)))
#print(f"Rezultat: {round(rezultat, 3)}")