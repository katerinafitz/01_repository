# Napiš funkci total_price, která vypočte cenu noci v hotelu. 
# Funkce bude mít dva parametry - persons a breakfast. 
# Cena za noc za osobu je 850 Kč a cena za snídani za osobu je 125 Kč. 
# Funkce vrátí výslednou cenu. Parametr breakfast je nepovinný a výchozí hodnota je False.
# Funkci vyzkoušej se zadáním dvou i jedné hodnoty, např. total_price(3), total_price(2, True).

def total_price (persons, breakfast = False):
    price_per_person = 850
    price_per_breakfast = 125
    # if breakfast == True: # == je jako is
    #     return persons * (price_per_person+price_per_breakfast)
    # else
    #     return persons * price_per_person

    if breakfast == True:
        return persons * (price_per_person + price_per_breakfast)
    return persons * price_per_person

persons = 2
price = total_price(persons)
