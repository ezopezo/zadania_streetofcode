### Program ktorý načíta list a opakujúce sa itemy vymaže (nielen duplicitné, ale celkovo). 
### Potrápilo, priznávam, dosť som sa zasekol na hlúpom spôsobe pridávania itemov do nového listu.

names = ['Jano', 'Jozko', 'Katka', 'Ferko', 'Jozko', 'Monika', 'Martin', 'Katka', 'Katka', 'Katka'] # List som si upravil, aby som si bol istý, že sú pokryté všetky možnosti.

def deduplicate(names):
    ''' Funkcia načíta list a vytvorí nový v ktorom sú odstránené opakujúce sa itemy. '''

    count_of_deleted = 0
    new_list = names.copy()         # Vytvoril som si kópiu listu z ktorého budem mazať itemy ak sa budú opakovať.

    for i in range(len(names)): 
        check = names[i]            # Do premennej check sa postupne ukladajú všetky itemy z listu...
        for name in names[i+1:]: 
            if name != check:       # ...a tu sa kontroluje premenná check so všetkými nasledujúcimi itemami v liste.
                continue            # Ak nie je check zhodný s nasledujúcim itemom kontroluje sa na ďalší.
            else:
                new_list.pop(i-count_of_deleted) # Ak je check zhodný s itemom, v new_list je item vymazaný na základe indexu odvodeného od iterátora...
                count_of_deleted += 1            # ...od ktorého je odpočítaný počet vymazaných itemov, ktorý sa tu navyšuje (ak sa vymaže item, indexy sa posúvajú).
                break

    return new_list


x = deduplicate(names)

print(x)



### Riešenie pomocou set-u.

def set_unique(names):
    ''' Funkcia načíta list, castne ho na set, čiže sa odstránia duplicity
    a castne set naspäť na list, ktorý vráti. Uf. Dlhší docstring jak funkcia.'''

    uniq_list = list(set(names)) # Set nemôže mať viac rovnakých hodnôt narozdiel od listu.

    return uniq_list


y = set_unique(names)

print(y)
