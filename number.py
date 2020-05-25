### Program ktorý načítava číselný vstup od užívateľa a po stlačení "q" vyráta priemer a sumu zo zadaných čísel.
### Ošetruje tiež chybný vstup pokiaľ užívateľ zadá char/string a tiež ak užívateľ nezadá dostatočné množstvo údajov. 
### Bez googlenia syntaxe za pár minút.

basket = [] # Inicializujem prázdny list do ktorého budem pridávať values.

while True:
    number = input("Zadaj cislo, alebo 'q' ak chces skoncit ")
    if number == "q": # Kontrola ukončenia programu
        break
    try:              # Pokiaľ sa znak dá castnuť na integer, tak sa pridá do listu, ak nie, tak program upozorní.
        basket.append(int(number))
    except ValueError:
        print('Prosim zadaj cislo alebo ukonci program s "q"!')

if len(basket) >= 1:  # Kontrola, či vôbec mám z čoho rátať.
    summary = sum(basket)
    average = sum(basket) / len(basket)
    print("")
    print("Suma je ", summary)
    print("Priemer je ", average)
else:
    print("")
    print("Nezadal si dostatok udajov, priemer a sucet nemoze byt vyratany!")


