n = int(input("Unesite prirodan broj: "))

while n != 1 and n != 4:
    zbir_kvadrata = 0
    while n > 0:
        cifra = n % 10
        zbir_kvadrata += cifra * cifra
        n //= 10
    n = zbir_kvadrata

if n == 1:
    print("dobar")
else:
    print("nije dobar")
