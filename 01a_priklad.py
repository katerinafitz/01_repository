# def get_mark(points):
#     if points <= 60:
#         mark = 5
#     elif points <= 70:
#         mark = 4
#     elif points <= 80:
#         mark = 3
#     elif points <= 90:
#         mark = 2
#     else:
#         mark = 1
#     return mark
# points = int(input("Zadej počet bodů v testu: "))
# mark = get_mark(points)
# if mark == 5:
#     points = int(input("Zadej počet bodů v opravném pokusu: "))
#     mark = get_mark(points)
# print(f"Výsledná známka je {mark}.")


# Napiš funkci mult, která bude mít dva číselné parametry. Funkce oba parametry vynásobí a vrátí výsledek.

# def mult_two_numbers (a,b):
#     return a*b

# result = mult_two_numbers (5,3)
# print(result)


# Převod kilometrů na míle a zpět
# Napište dvě funkce: kilometry_na_mile(kilometry) a mily_na_kilometry(mile), 
# které provedou převod mezi kilometry a mílemi.

# def kilometry_na_mile (a,b):
#     return a/b
# result = kilometry_na_mile (1,1.609344)
# print(result)

# def mile_na_kilometry(a,b):
#     return a*b
# result = mile_na_kilometry (1,1.609344)
# print(result)


#Napiš funkci, která jako parametr převezme řetězec a vytiskne jej obalen hvězdičkami.

def hvezda(slovo):
    return f'{(2 * len(slovo)*'*')}\n* {slovo} *\n{(2 * len(slovo)*'*')}'
print(hvezda('ahoj'))
    
