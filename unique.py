### Funkcia načíta list do nového listu naháže itemy, ktoré sa vyskytujú iba raz.
### Nakódené za 30 min. Nevravím, že to je najlepší a najčitateľnejší spôsob, ale je to funkčný spôsob.

def unique(list_dupl):
    ''' Funkcia vytiahne z listu itemy, ktoré sa v ňom vyskytujú iba raz. '''

    count_of_incidence = 0
    uniq_list = []          # Sem sa budú hádzať unikátne itemy.

    for i in range(len(list_dupl)):     # Podobná konštrukcia ako pri deduplicate - do premennej chceck postupne ukladám itemy z listu.
        check = list_dupl[i]

        if count_of_incidence > 1:      # Počas prvej iterácie tento blok neplatí - count_of_incidence = 0. Počas druhej musí mať premenná hodnotu aspoň 1.
            count_of_incidence = 0      # Ak má count_of_incidence hodnotu väčšiu ako 1, tak sa iba vynuluje a ide sa na ďalší item.
        elif count_of_incidence == 1: 
            uniq_list.append(list_dupl[i-1]) # Ak má hodnotu práve 1, tak sa do nového listu pridá predchádzajúca hodnota (pretože iterátor je už nastavený na hodnotu o číslo väčšiu).
            count_of_incidence = 0           # ...a count_of_incidence musí byť zase vynulovaný.

        for item in list_dupl:          # Znova iterujem cez celý list.
            if item == check:           # Ak sa item rovná check, priráta sa do count_of_incidence 1 a pokračuje sa iterovaním cez list.
                count_of_incidence += 1    
                continue
    
    if count_of_incidence == 1:         # Somarinka, v prípade, že unikátny item je posledný v liste.
        uniq_list.append(list_dupl[i])
    
    return uniq_list


x = unique([1, 9, 8, 8, 7, 6, 1, 6, 2])

print(x)

