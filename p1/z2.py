##napisati program koji od korisnika traži unos prirodnog broja n,a zatim unos n rijeci.Nakon toga program ispisuje onu
# rijec koja je imala najvise razlicitih samoglasnika u sebi (ako ih je vise, ispisuje onu od njih koja je najkasnije unesena),
# te koliko razlicitih samoglasnika ta rijec sadrzi.Možete pretpostaviti da su u unesenim riječima sva slova mala.
n=int(input("Unesite prirodni broj n: "))
rijeci = ""
najveci_broj_samoglasnika = 0

for i in range(n):
    rijec = input(f"Unesite {i+1}. rijec: ").lower()
    rijeci += rijec + " "
    samoglasnici = set("aeiou")
    broj_samoglasnika = sum(1 for slovo in rijec if slovo in samoglasnici)
    if broj_samoglasnika > najveci_broj_samoglasnika:
        najveci_broj_samoglasnika = broj_samoglasnika
        najkasnija_rijec : str = rijec
print(f"rijec s anajvise samoglasnika je {najkasnija_rijec} i ima {najveci_broj_samoglasnika} samoglasnika")


