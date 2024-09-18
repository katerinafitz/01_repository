# rozcvicka
# Vypocti a zobraz cenu jedne noci v hotelu pro zadany pocet osob
# cena za noc za jednu osobu je 850 Kc, na pocet osob se zeptej uzivatele

pocet_osob = int(input("Zadej počet osob: "))
cena_za_noc = 850

cena_vysledna = pocet_osob * cena_za_noc
print(cena_vysledna)