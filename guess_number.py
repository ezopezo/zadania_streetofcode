### Program má za úlohu čo najefektívnejšie hádať číslo na ktoré myslím.
### Trochu potrápilo. Samotné core bolo pomerne jednoduché, horšie boli kontroly:
### Aby sa nedalo zadať väčšie ako 100, menšie ako 1 a tiež aby počítač nehádal dookola tie isté čísla.
### A áno uvedomujem si, že používanie globálnych premenných je bad practice. Je na tvojom zvážení, či sú tu adekvátne, rád o tom podiskutujem.

guess = 50
iterator = -1                       # Vytvorený "pseudoiterátor" vysvetlený dole.
steps = [25, 12, 6, 3, 2, 1, 1, 1]  # Vytvorený list s hodnotami, ktoré budú funkcie lower a higher odrátavať, prirátavať, podľa počtu guess-ov.
attempts = [guess]

### Inicializácia hry. Program začína hádať číslom 50.
print("Mysli si cislo od 1 po 100 a ja budem hadat.")
print("Je cislo na ktore myslis vacsie, mensie alebo je to ", guess, "? Zadaj 'm' ak je cislo mensie, 'v' ak je cislo vacsie a hocijaku klavesu ak som trafil.")
nav = input()


### Funkcie na úpravu guess-u podľa výstupu z controllera.
def lower(guess):
    global iterator, steps, attempts # Globálne premenné si zvyknem inicializovať v prvej funkcii...
    guess = guess - steps[iterator] # Tu je pseudoiterátor využitý na prechod cez list s hodnotami a odrátava ich od guess-u. Hodnoty sú závislé na to koľký to je guess.
    x = input_control(guess)        # Presmmerovanie na funkciu input_control, ktorá overí, či je vstup validný.
    if x == False:
        return False                # Ak sú podmienky nesplnené input_control vyhodí chybovú hlášku a program končí.
    else:
        print("Je cislo na ktore myslis vacsie, mensie alebo je to ", guess, "? Zadaj 'm' ak je cislo mensie, 'v' ak je cislo vacsie a hocijaku klavesu ak som trafil.")
    attempts.append(guess)          # Pridanie guess-u počítača do listu. Funkcia input_control overuje, či guess už počítač nehádal.
    nav = input()                   # Funkcia žada tiež užívateľa o ďalšiu navigáciu.

    return controller(nav, guess)

def higher(guess):
    guess = guess + steps[iterator]
    x = input_control(guess)
    if x == False:
        return False
    else:
        print("Je cislo na ktore myslis vacsie, mensie alebo je to ", guess, "? Zadaj 'm' ak je cislo mensie, 'v' ak je cislo vacsie a hocijaku klavesu ak som trafil.")
    attempts.append(guess)   
    nav = input() 

    return controller(nav, guess)


### Kontroluje, či sú ešte čísla v rozmedzí od 1 po 100 a či opäť neháda už spomenuté číslo. 
def input_control(guess):
    if guess != 101 and guess != 0:
        for item in attempts[:-1]: # Preiteruje list okrem posledného prvku a skontroluje, či program zbytočne neháda už hádané číslo.
            if guess != item:
                continue
            else:
                print("")
                print("Cislo som uz spomenul! Niekde si sa pomylil.")
                return False
    else:
        print("")
        print("Cislo na ktore myslis je evidentne mimo zadaneho rozsahu. Zadanie bolo mysliet na cislo od 1 do 100.")
        return False
        

### Controller hry. Spracúva input užívateľa a volá na základe toho funkcie, ktoré upravujú guess.
def controller(nav, guess):
    global iterator
    if nav == 'm':    # Menšie.
        iterator += 1 # Vytvorený pseudoiterátor, ktorý ráta počet pokusov. Nastavený je deflaut na -1 aby po prirátaní mohol odkazovať na prvé číslo v steps liste.
        lower(guess)
    elif nav == 'v':  # Väčšie.
        iterator += 1
        higher(guess)
    else:
        print('Takze som uhadol? Najs! Cislo na ktore si myslel je', guess, '!') # Stlačením čohokoľvek okrem 'm' a 'v' program končí s predpokladom, že uhádol číslo.
        print('Pocet pokusov, ktore som potreboval:', iterator+2)                # Tiež uvedie počet pokusov ktoré mu boli treba na uhádnutie.


controller(nav, guess)
