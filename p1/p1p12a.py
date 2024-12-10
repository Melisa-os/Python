n = int(input("Unesite broj: "))
print("Najbolji", end=" ")

brojac = 0

if n % 1 == 0:
    print("najsjajniji", end=", ")
    brojac += 1
if n % 2 == 0:
    print("najuzbudljiviji", end=", ")
    brojac += 1
if n % 3 == 0:
    print("najfantasticniji", end=", ")
    brojac += 1
if n % 4 == 0:
    print("najkrasniji", end=", ")
    brojac += 1
if n % 5 == 0:
    print("najljepsi", end=", ")
    brojac += 1
if n % 6 == 0:
    print("najemotivniji", end=", ")
    brojac += 1
if n % 7 == 0:
    print("najsrdacniji", end=", ")
    brojac += 1
if n % 8 == 0:
    print("najfiniji", end=", ")
    brojac += 1
if n % 9 == 0:
    print("najjasniji", end=", ")
    brojac += 1
if n % 10 == 0:
    print("najinspirativniji", end=", ")
    brojac += 1

print(f"broj je {n}!")
print(brojac)
