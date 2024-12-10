# Unos broja n
n = int(input("Unesite prirodni broj n: "))

# Početna pozicija zmije
x, y = 0, 0

# Broj poteza
broj_poteza = 2 * (n - 1)

# Početna matrica
for i in range(n):
    for j in range(n):
        if i == x and j == y:
            print('*', end=' ')
        else:
            print('-', end=' ')
    print()

# Unos poteza zmije (H za horizontalno, V za vertikalno)
for _ in range(broj_poteza):
    potez = input().strip()
    if potez == 'H':
        y += 1
    elif potez == 'V':
        x += 1

    # Iscrtavanje matrice posle svakog poteza
    for i in range(n):
        for j in range(n):
            if (i < x or (i == x and j <= y)):
                print('*', end=' ')
            else:
                print('-', end=' ')
        print()

