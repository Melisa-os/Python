n = int(input("Unesite broj: "))

if n <= 1:
    print(f"{n} nije složen broj.")
else:
    slozen = False
    for i in range(2, n):
        if n % i == 0:
            slozen = True
            break

    if slozen:
        print(f"{n} je složen broj.")
    else:
        print(f"{n} nije složen broj.")
