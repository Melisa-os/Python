n = int(input("Unesite broj: "))

if n <= 1:
    print(f"{n} nije prost broj.")
else:
    prost = True
    for i in range(2, n):
        if n % i == 0:
            prost = False
            break

    if prost:
        print(f"{n} je prost broj.")
    else:
        print(f"{n} nije prost broj.")
