while True:
  n = input("Unesite prirodan broj n: ")
  if len(n) % 2 != 0:
      print("Broj mora imati paran broj cifara.")
  else :
      break
zbir = 0
i = 0
while i < len(n) - 1:
        dvocifreni_broj = int(n[i]) * 10 + int(n[i + 1])
        zbir += dvocifreni_broj
        i =i+2
print("Zbir dvocifrenih brojeva sastavljenih od po dvije susjedne cifre:", zbir)
print ("Kraj programa")
