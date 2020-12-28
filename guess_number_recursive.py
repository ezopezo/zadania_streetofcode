#guess_number_recursive

def give_range_of_numbers():
    while True:
        try: 
            played_range = int(input('Please provide range of numbers for playing: ')) / 2 # initial halving
        except ValueError:
            print('Please provide number.')
            continue
        else:
            return played_range 

fraction = give_range_of_numbers()                                         # preparing instances for global variables
guesses = set()

def acquire_valid_guess(number):
    global guesses              

    if (number not in guesses) and (number > 0):
        guesses.add(round(number))
        print('Is number higher or lower than', round(number), '?')
        answer = input('Type "h" if higher or "l" if lower or "enter" if it is a number that you think: ')
        return answer
    else:
        return False


def guess_recursive(number):
    global fraction
    fraction = fraction / 2
    answer = acquire_valid_guess(number) 

    while True:
        if answer == 'h':     return guess_recursive(round(number + fraction))   
        elif answer == 'l':   return guess_recursive(round(number - fraction)) 
        elif answer == '':    return print('Done! I needed', str(len(guesses)), 'attempts to guess your number!')  
        elif answer == False: return print('This number has been guessed already, or it is out of range of played numbers!')
        else:                 answer = input('Type "h" if higher or "l" if lower, or "enter" for intended number: ')
            
    return number



guess_recursive(fraction)