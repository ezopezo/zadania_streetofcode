### Program ktorý načíta kameň papier alebo naožnoce od dvoch hráčov a určí víťaza.
### Ošetrené aby sa nedali zadať písmená, alebo čísla mimo.
### Vygooglené iba aby sa pokus prvého hráča nezobrazil, aby hra mala reálne použitie. 

import getpass

print('''Vitaj v hre hip-hap-hop pre 2 hracov. Najprv vypisem moznosti, a potom zada vyber prvy hrac a za nim druhy hrac.
    1. kamen
    2. papier
    3. noznice
''')

print("Prvy hrac ")
while True:                                                                  # Pre oboch hráčov kontroly, aby sa nezadávali čísla mimo, alebo chars/stringy.
    first_player = getpass.getpass("Vyber moznost (musi byt medzi 1 az 3) ") # Input, ktorý ostane skrytý aby druhý hráč nevidel pokus prvého hráča.
    try: 
        if int(first_player) in range(1,4):
            first_player = int(first_player)
            break
        else: 
            print("Zadaj číslo od 1 do 3!")
    except ValueError:
        print("Zadaj číslo od 1 do 3! Text nie je akceptovaný.")

print("")
print("Druhy hrac ")
while True:
    second_player = input("Vyber moznost (musi byt medzi 1 az 3) ")
    try:
        if int(second_player) in range(1,4):
            second_player = int(second_player)
            break
        else: 
            print("Zadaj číslo od 1 do 3!")
    except ValueError:
        print("Zadaj číslo od 1 do 3! Text nie je akceptovaný.")

print("")

# Core hry.
if first_player == 1 and second_player == 2: # 1. kamen, 2. papier
    print("Vyhral druhy hrac!")
elif first_player == 2 and second_player == 1: # 1. papier, 2. kamen
    print("Vyhral prvy hrac!")
elif first_player == 3 and second_player == 1: # 1. noznice, 2. kamen
    print("Vyhral druhy hrac!")
elif first_player == 1 and second_player == 3: # 1. kamen, 2. noznice
    print("Vyhral prvy hrac!")
elif first_player == 2 and second_player == 3: # 1. papier, 2. noznice
    print("Vyhral druhy hrac!")
elif first_player == 3 and second_player == 2: # 1. noznice, 2. papier
    print("Vyhral prvy hrac!")
elif first_player == second_player: # remíza
    print("Remíza!")